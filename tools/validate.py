#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate a packaged OPEN-RPGFXS directory without external dependencies."""
from pathlib import Path
import json,hashlib,struct,wave,argparse

def validate(root):
 read=lambda p:json.loads((root/p).read_text(encoding='utf-8'));m=read('doc/manifest.json');errors=[];count=0;seenpcm={};seenpng={}
 def check(ok,msg):
  if not ok:errors.append(msg)
 for code,path in m['animations'].items():
  a=read(path);p=root/a['file'];b=p.read_bytes();check(b[:8]==b'\x89PNG\r\n\x1a\n',code+' PNG');w,h=struct.unpack('>II',b[16:24]);check(w==a['columns']*384 and h==a['rows']*384,code+' canvas');check(b[25]==6,code+' RGBA');check(hashlib.sha256(b).hexdigest()==a['file_sha256'],code+' hash');check(a['frame_count']==len(a['frames']),code+' frames');check(abs(sum(f['duration_ms'] for f in a['frames'])-a['recommended_duration_ms'])<.01,code+' duration');check(a['sequence_sha256'] not in seenpng,code+' duplicate sequence');seenpng[a['sequence_sha256']]=code
  for f in a['frames']:check(f['x']>=0 and f['y']>=0 and f['x']+f['w']<=w and f['y']+f['h']<=h,code+' frame bounds')
  for pair in a['pairings']:check(pair in m['pairings'],code+' pair reference')
  count+=1
 for code,path in m['audio'].items():
  a=read(path);p=root/a['file'];check(hashlib.sha256(p.read_bytes()).hexdigest()==a['sha256'],code+' file hash')
  with wave.open(str(p),'rb') as w:
   check((w.getframerate(),w.getnchannels(),w.getsampwidth())==(48000,2,2),code+' WAV format');check(w.getnframes()==a['format']['samples'],code+' samples');payload=w.readframes(w.getnframes())
  sha=hashlib.sha256(payload).hexdigest();check(sha==a['pcm_sha256'],code+' PCM hash');check(sha not in seenpcm,code+' duplicate PCM');seenpcm[sha]=code;check(a['metrics']['sample_peak_dbfs']>-110,code+' silence');count+=1
 for code,path in m['pairings'].items():
  p=read(path);check(p['review']['decision']=='좋음' and p['review']['source_bound'],code+' review');check(p['animation'] in m['animations'],code+' animation');check(bool(p['routes']),code+' audio')
  for e in p['routes']:
   check(e['audio'] in m['audio'],code+' sound reference');check(e['duration_ms']>0 and e['gain']>0,code+' playback');check(abs(e['start_ms']+e['duration_ms']-e['end_ms'])<.001,code+' timing')
  check(p['signal']['sample_peak_dbfs']<.01,code+' mix clipping');count+=1
 integrity=root/'doc/integrity.json'
 if integrity.exists():
  for r in read('doc/integrity.json')['files']:
   p=root/r['path'];check(p.is_file(),r['path']+' missing')
   if p.is_file():check(p.stat().st_size==r['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],r['path']+' integrity')
 return {'schema':'open-rpgfxs.validation/1','objects_checked':count,'counts':m['counts'],'errors':errors,'ok':not errors,'note':'Structural/hash/PCM checks. The packaging build also compared every sheet cell against the source frames and measured routed audio; this command does not grant new human approval.'}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);args=ap.parse_args();r=validate(args.root);print(json.dumps(r,ensure_ascii=False,indent=2));raise SystemExit(0 if r['ok'] else 1)
