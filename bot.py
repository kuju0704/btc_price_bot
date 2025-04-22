import requests
import os
import time
from datetime import datetime, timedelta

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    response = requests.get(url, params=params)
        print(response.text)
    return response.json()["bitcoin"]["usd"]

def send_to_discord(message):
    data = {"content": message}
    requests.post(DISCORD_WEBHOOK_URL, json=data)

def main():
    now = datetime.utcnow()
    one_hour_ago = now - timedelta(hours=1)
    
    price_now = get_btc_price()
    time.sleep(5)
    price_before = get_btc_price()

    diff = price_now - price_before
    status = "上昇" if diff > 0 else "下落" if diff < 0 else "変化なし"

    message = (
        f"【BTC価格通知】\n"
        f"現在価格：${price_now:,.2f}\n"
        f"1時間前との差：{status}（${abs(diff):,.2f}）"
    )
    send_to_discord(message)

if __name__ == "__main__":
    main()