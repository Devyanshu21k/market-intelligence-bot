import pandas as pd

def get_gainers():

    url = "https://www1.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.csv"

    df = pd.read_csv(url)

    return df.head(5)[["symbol","pChange"]]


def get_losers():

    url = "https://www1.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.csv"

    df = pd.read_csv(url)

    return df.head(5)[["symbol","pChange"]]
