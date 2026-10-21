---
name: python-api-trend
description: >-
  LG전자(066570) 및 주요 LG 계열사(LG이노텍 011070, LG디스플레이 034220, LG에너지솔루션 373220) 실시간 주가·등락률(네이버 금융),
  글로벌 실시간 환율(USD/KRW, EUR, JPY), 구글 뉴스 'LG전자 AI 가전' 최신 헤드라인 5건을 수집하는 라이브 마켓 대시보드 데이터 스킬.
  실시간 시장 지표나 최신 뉴스 대시보드를 조회·연동할 때 사용한다.
---

# LG Live Market Dashboard Data Skill (`python-api-trend`)

이 스킬은 외부 유료 API 키 없이 파이썬 표준 라이브러리(`urllib`, `json`, `xml.etree.ElementTree`)만을 사용하여 LG전자 및 주요 LG 계열사 멀티 티커 주가, 환율, 최신 뉴스 헤드라인을 수집합니다.

## 포함 스크립트

- [fetch_lg_live_market.py](./scripts/fetch_lg_live_market.py)
  - `fetch_lg_live_dashboard_data(stock_code="066570", keyword="LG전자 AI 가전")` 함수를 제공합니다.
  - 수집 항목:
    1. **네이버 금융 LG 계열사 멀티 티커 실시간 주가·등락률 (`affiliate_tickers`)**:
       - `066570` (LG전자), `011070` (LG이노텍), `034220` (LG디스플레이), `373220` (LG에너지솔루션)
    2. **글로벌 실시간 환율 (`api.frankfurter.dev`)**: `usd_krw`, `eur_krw`
    3. **구글 뉴스 RSS 최신 헤드라인 5건**: `latest_news` (`title`, `pubDate`, `link` 리스트)

## 실행 및 활용 방법

1. 터미널에서 직접 실행하여 JSON 데이터를 가져올 때:
   ```powershell
   python .agents/skills/python-api-trend/scripts/fetch_lg_live_market.py
   ```
2. 다른 파이썬 코드에서 임포트하여 사용할 때:
   ```python
   from fetch_lg_live_market import fetch_lg_live_dashboard_data
   data = fetch_lg_live_dashboard_data()
   ```
3. 대시보드 UI(`index.html` 등)를 생성하거나 업데이트할 때 위 스크립트를 실행해 실시간 데이터를 주입하거나, 동일한 엔드포인트 구조를 활용합니다.
