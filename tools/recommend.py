#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Offline heuristic SFX retrieval. Python standard library only."""
from pathlib import Path
import argparse,json,math

def load(root):
 read=lambda name:json.loads((root/name).read_text(encoding='utf-8'))
 return read('doc/query-catalog.json'),read('doc/package-code-map.json'),read('doc/keyword-map.json')

def resolve_pair(catalog,codes,value):
 value=codes['aliases'].get(value,{}).get('pairing',value)
 p=next((p for p in catalog['pairings'] if p['code']==value),None)
 if p is None:raise ValueError('Unknown pairing/source ID: '+str(value))
 return p

def canonical(query,keywords):
 q=query.lower().replace('물리','physical').replace('돌격','charge');return set(c['id'] for c in keywords['concepts'] if c['id'] in q or any(a.lower() in q for a in c['aliases']))

def allowed(sound,target):
 # Exact reviewed use remains valid, even when this source failed another context.
 if target and target['code'] in sound['pairings']:return True
 for r in sound.get('reuse_restrictions',[]):
  if r.get('reuse_blocked'):return False
  if target and (target['source_id'] in r.get('reuse_rejected_contexts',[]) or target['group'] in r.get('reuse_disallowed_families',[])):return False
 return True

def rank(catalog,keywords,target=None,query='',level=None,top=10,event=1,exclude=None):
 tags=set(target['concepts'] if target else [])|canonical(query,keywords);level=level if level is not None else (target or {}).get('level')
 desired=(target or {}).get('timing',{}).get('temporal_pattern');results=[]
 targetroute=target['routes'][min(max(1,event),len(target['routes']))-1] if target else None
 target_count=len(target['timing']['impact_events']) if target and len(target['routes'])==1 else 1
 target_intervals=target['timing']['impact_intervals_ms'] if target and len(target['routes'])==1 else []
 if target and len(target['routes'])>1 and desired=='sequence':desired='one-shot'
 sound_by_id={s['code']:s for s in catalog['audio']};pair_by_id={p['code']:p for p in catalog['pairings']}
 strength_target=target
 if target and level is not None:
  group=[p for p in catalog['pairings'] if p['group']==target['group'] and p.get('level')==level]
  if group:strength_target=next((p for p in group if p['role']=='primary'),group[0])
 strength_route=strength_target['routes'][min(max(1,event),len(strength_target['routes']))-1] if strength_target else None
 elements={'fire','water','ice','rock','electric','poison','smoke','shadow','light','wind'}
 for s in catalog['audio']:
  if not allowed(s,target):continue
  if set(exclude or [])&set(s['concepts']):continue
  have=set(s['concepts']);shared=tags&have;reasons=[];score=0.
  # Canonical concepts are counted once, regardless of alias or prompt frequency.
  for tag in sorted(shared):
   points=12 if tag in elements else 8 if tag in {'arrow','knife','slash','blunt','heal','shield'} else 4
   score+=points;reasons.append({'factor':tag,'points':points})
  if tags&elements and have&elements and not tags&have&elements:score-=24;reasons.append({'factor':'element mismatch','points':-24})
  exact=bool(target and target['code'] in s['pairings'])
  if exact:score+=100;reasons.append({'factor':'reviewed exact pairing','points':100})
  elif target and any(p['animation']==target['animation'] and p['code'] in s['pairings'] for p in catalog['pairings']):score+=32;reasons.append({'factor':'reviewed same sprite sequence','points':32})
  if desired:
   patterns=s.get('slot_patterns',[]);fits=[p for p in patterns if p['pattern']==desired]
   pts=15 if fits else -18;score+=pts;reasons.append({'factor':'temporal use pattern per audio slot','points':pts})
   if target_count and patterns:
    nearest=min(patterns,key=lambda p:abs(p['event_count']-target_count));pts=10 if nearest['event_count']==target_count else -min(20,abs(nearest['event_count']-target_count)*6);score+=pts;reasons.append({'factor':'reviewed event count (not waveform peak count)','points':pts})
    if target_intervals and len(nearest['intervals_ms'])==len(target_intervals):
     error=sum(abs(a-b) for a,b in zip(target_intervals,nearest['intervals_ms']))/len(target_intervals);pts=max(-15,10-error/25);score+=pts;reasons.append({'factor':'event interval mean absolute error ms','value':round(error,3),'points':round(pts,2)})
  levels=s.get('usage_levels',[])
  if level is not None and levels:
   pts=12*(1-min(abs(level-l) for l in levels)/98);score+=pts;reasons.append({'factor':'reviewed usage level proximity','points':round(pts,2)})
  if targetroute:
   ref=targetroute['duration_ms'];diff=abs(math.log(max(1,s['metrics']['duration_ms'])/max(1,ref)))
   pts=max(-12,8-8*diff);score+=pts;reasons.append({'factor':'duration proximity (tail allowed)','points':round(pts,2)})
  if strength_route:
   ref=sound_by_id[strength_route['audio']];refgain=20*math.log10(max(1e-8,strength_route['gain']))
   usages=[pair_by_id[pc] for pc in s['pairings']]
   uses=sorted(usages,key=lambda p:(p['group']!=target['group'],abs((p.get('level') or 50)-(level or 50))))
   use_route=next(r for r in uses[0]['routes'] if r['audio']==s['code']);use_gain=20*math.log10(max(1e-8,use_route['gain']))
   for metric in ['sample_peak_dbfs','active_rms_dbfs']:
    diff=(s['metrics'][metric]+use_gain)-(ref['metrics'][metric]+refgain);pts=max(-10,6-abs(diff)/3);score+=pts;reasons.append({'factor':metric+' proximity at reviewed gains','delta_db':round(diff,3),'points':round(pts,2)})
  plan=None
  if targetroute:
   local=s['metrics']['main_onset_candidate_ms'];anchor=targetroute.get('target_event_ms');delta=targetroute.get('main_onset_delta_ms')
   start=anchor+(delta or 0)-local if anchor is not None else targetroute['start_ms']
   current=next(x for x in catalog['audio'] if x['code']==targetroute['audio'])
   gain_db=20*math.log10(max(1e-8,targetroute['gain']))+current['metrics']['active_rms_dbfs']-s['metrics']['active_rms_dbfs']
   gain_db=min(gain_db,-3-s['metrics']['sample_peak_dbfs'])
   gain_db=max(-24,min(12,gain_db))
   exact_route=next((r for r in (target or {}).get('routes',[]) if r['audio']==s['code']),None)
   plan={'replace_event':event,'audio':s['code'],'start_ms':round(start,3),'gain_suggestion':round(10**(gain_db/20),6),'new_main_onset_candidate_ms':local,'anchor_event_ms':anchor,'preserved_reviewed_main_onset_delta_ms':delta,'status':'heuristic; audition onset, material and mixture headroom; do not apply automatically','audio_end_ms':round(start+s['metrics']['duration_ms'],3),'tail_after_visual_ms':round(max(0,start+s['metrics']['duration_ms']-target['timing']['duration_ms']),3)}
   if exact_route:plan={'status':'reviewed exact route','route':exact_route}
  results.append({'audio':s['code'],'name_ko':s['name_ko'],'file':s['file'],'score':round(score,3),'review_status':'reviewed exact use' if exact else 'recommendation only','duration_ms':s['metrics']['duration_ms'],'usage_levels':levels,'sample_peak_dbfs':s['metrics']['sample_peak_dbfs'],'active_rms_dbfs':s['metrics']['active_rms_dbfs'],'reasons':reasons,'replacement_draft':plan,'best_use':s['best_use'][:4]})
 results.sort(key=lambda x:(-x['score'],x['audio']))
 return results[:top]

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--pairing',help='ORFX...-Pxx or original source ID, e.g. rpg-01-l50');ap.add_argument('--query',default='');ap.add_argument('--level',type=int,choices=[1,25,50,75,99]);ap.add_argument('--top',type=int,default=10);ap.add_argument('--event',type=int,default=1)
 ap.add_argument('--exclude',action='append',default=[],help='Hard-exclude canonical concept or aliases, e.g. fire or 불. Repeatable; natural-language negation is not parsed.')
 args=ap.parse_args();catalog,codes,keywords=load(args.root);target=resolve_pair(catalog,codes,args.pairing) if args.pairing else None
 if not target and not args.query:ap.error('Use --pairing or --query')
 excludes=set().union(*(canonical(x,keywords) for x in args.exclude)) if args.exclude else set()
 print(json.dumps({'schema':'open-rpgfxs.recommendations/1','algorithm':'canonical-context-timing-v1','target':target['code'] if target else None,'query':args.query,'excluded_concepts':sorted(excludes),'results':rank(catalog,keywords,target,args.query,args.level,args.top,args.event,excludes),'note':'Sample amplitude, active RMS and reviewed level are different factors. Max peak is never treated as a semantic contact. Several detected waveform peaks may be a single sound tail.'},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
