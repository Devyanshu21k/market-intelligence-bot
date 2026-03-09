import feedparser

feeds = [
"https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
"https://www.moneycontrol.com/rss/business.xml"
]

def get_news():

    news = []

    for url in feeds:

        feed = feedparser.parse(url)

        for entry in feed.entries[:3]:

            news.append(entry.title)

    return news[:5]
