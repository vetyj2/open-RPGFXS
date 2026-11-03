# 추천 방법과 재생 계약

canonical-context-timing-v1은 검수 통과된 WAV만 대상으로 계산합니다. 결과 점수는 확률이나 100점 만점이 아닙니다.

- 정규화한 속성 키워드 일치 +12, 화살/검/둔격/치유/보호 +8, 기타 동작 +4. 동의어는 한 번만 계산합니다. 속성 불일치 -24.
- 같은 조합의 검수 음원 +100, 같은 이미지의 다른 통과 조합 +32.
- 슬롯의 단발/연타/지속 패턴 +15, 불일치 -18. 연타 전용 파일과 여러 단발 파일은 별개입니다.
- 기록된 타격 수 일치 +10, 차이당 -6(최대 -20). 간격 수가 같으면 평균 오차 25ms당 1점을 감점합니다(+10부터 최소 -15). 파형 피크 개수를 의미상 타격 개수로 확정하지 않습니다.
- 사용 레벨 근접도 최대 +12. 생성 순서로 레벨을 정하지 않습니다.
- 길이는 로그 비율로 +8부터 감점하며 자연 잔향을 허용합니다. 애니메이션 길이와 같아야 한다는 필터는 없습니다.
- 검수된 gain에서 sample peak와 active RMS 근접도를 각각 최대 +6 반영합니다. 재질/질량/힘의 절대 척도로 간주하지 않습니다.
- 원음 재사용 금지 문맥은 제외합니다. 그 원음의 정확한 통과 조합은 보존합니다. `--exclude fire` 같은 명시 제외 키워드는 강제 필터입니다. 자연어의 부정 표현은 자동 해석하지 않습니다.

교체 초안은 main_onset 후보와 검수된 상대 시차를 이용합니다. 더 높은 레벨을 요청하면 해당 계열의 실제 통과 레벨을 신호 비교 기준으로 삼습니다. 추천 게인은 개별 파일의 -3dBFS 여유를 고려하나 여러 파일이 겹친 합성은 다시 검사해야 합니다. gain만 올린 것은 새 거대 재질 사운드가 아닙니다.

## 엔진 재생 의사코드

```text
pair = resolve(source_id or pairing_code)
clock_zero = engine_time + max(0, -min(route.start_ms))
for route in pair.routes:
    play(route.file, at=clock_zero+route.start_ms, gain=route.gain)
    # 파일 자체에 자름과 페이드 적용 완료. 추가 skip/fade 없음.
for frame in animation.frames:
    draw(sprite_rect=frame, at=clock_zero+frame.start_ms,
         hold=frame.duration_ms, pivot=(192,192), filter=nearest)
clear_sprite(at=clock_zero+animation.recommended_duration_ms)
# 오디오는 각 파일 종료까지. 짧게 자르는 새 변경은 별도 검수.
```

`start_sample_48k`는 기준 시계에서의 샘플 위치입니다. 가변 프레임의 변경 시각은 원래 합성의 변경 시각을 보존합니다. `nearest_display_time_ms`와 `time_ms`가 다르면 전자는 샘플 프레임, 후자는 연속 저작 시계의 접촉입니다. 양쪽을 구분하여 판정을 구현하세요.
