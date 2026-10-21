import urllib.request, urllib.parse, json, ssl, xml.etree.ElementTree as ET

LG_AFFILIATE_CODES = [
    ("066570", "LG전자"),
    ("011070", "LG이노텍"),
    ("034220", "LG디스플레이"),
    ("373220", "LG에너지솔루션"),
]

def _get(url):
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=5, context=ctx).read()

def fetch_stock_quote(code, default_name=""):
    stock = json.loads(_get(f"https://m.stock.naver.com/api/stock/{code}/basic").decode("utf-8"))
    return {
        "stock_code": code,
        "stock_name": stock.get("stockName", default_name),
        "close_price": stock.get("closePrice"),
        "compare_to_previous_price": stock.get("compareToPreviousClosePrice"),
        "fluctuation_rate": stock.get("fluctuationsRatio"),
    }

def fetch_lg_live_dashboard_data(stock_code="066570", keyword="LG전자 AI 가전"):
    # 1. 네이버 금융 LG 주요 계열사 멀티 티커 실시간 주가·등락률 조회
    affiliates = [fetch_stock_quote(code, name) for code, name in LG_AFFILIATE_CODES]
    primary = next((item for item in affiliates if item["stock_code"] == stock_code), affiliates[0])

    # 2. 글로벌 실시간 환율(USD/KRW, EUR, JPY) 조회
    fx = json.loads(_get("https://api.frankfurter.dev/v1/latest?base=USD&symbols=KRW,EUR,JPY").decode("utf-8"))

    # 3. 구글 뉴스 실시간 'LG전자 AI 가전' 최신 헤드라인 5건 조회
    rss_url = f"https://news.google.com/rss/search?q={urllib.parse.quote(keyword)}&hl=ko&gl=KR&ceid=KR:ko"
    root = ET.fromstring(_get(rss_url))
    news = [{"title": item.findtext("title"), "pubDate": item.findtext("pubDate"), "link": item.findtext("link")} for item in root.findall(".//item")[:5]]
    usd_krw = round(fx["rates"]["KRW"], 2)
    eur_krw = round(fx["rates"]["KRW"] / fx["rates"]["EUR"], 2)

    return {
        "stock_name": primary["stock_name"],
        "stock_code": primary["stock_code"],
        "close_price": primary["close_price"],
        "compare_to_previous_price": primary["compare_to_previous_price"],
        "fluctuation_rate": primary["fluctuation_rate"],
        "affiliate_tickers": affiliates,
        "usd_krw": usd_krw,
        "eur_krw": eur_krw,
        "fx_date": fx.get("date"),
        "latest_news": news
    }

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    data = fetch_lg_live_dashboard_data()
    print(json.dumps(data, ensure_ascii=False, indent=2))
