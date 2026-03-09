import os
import requests

from market_data import get_indices
from gainers_losers import get_gainers,get_losers
from news_fetcher import get_news
from sentiment import calculate_sentiment


BOT_TOKEN = os.environ["TG_TOKEN"]
CHAT_ID = os.environ["TG_CHAT"]


def send_telegram(msg):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url,data={
        "chat_id":CHAT_ID,
        "text":msg,
        "parse_mode":"Markdown"
    })


def build_message():

    indices = get_indices()

    gainers = get_gainers()
    losers = get_losers()

    news = get_news()

    sentiment = calculate_sentiment(indices)

    msg = "📊 *Indian Market Close*\n\n"

    for name,data in indices.items():

        msg += f"{name}: {data['change']}%\n"

    msg += "\n📈 *Top Gainers*\n"

    for _,row in gainers.iterrows():

        msg += f"{row['symbol']} {row['pChange']}%\n"

    msg += "\n📉 *Top Losers*\n"

    for _,row in losers.iterrows():

        msg += f"{row['symbol']} {row['pChange']}%\n"

    msg += "\n🧠 *Market Sentiment:* " + sentiment

    msg += "\n\n📰 *Key News*\n"

    for n in news:

        msg += f"• {n}\n"

    return msg


if __name__ == "__main__":

    message = build_message()

    send_telegram(message)
