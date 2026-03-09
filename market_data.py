import requests

def get_index(symbol):

    url = f"https://priceapi.moneycontrol.com/pricefeed/notapplicable/inidicesindia/{symbol}"

    r = requests.get(url)
    data = r.json()["data"]

    return {
        "price": data["pricecurrent"],
        "change": float(data["pricepercentchange"])
    }


def get_indices():

    indices = {
        "NIFTY 50": "in%3BNSEI",
        "BANK NIFTY": "in%3NNSEBANK",
        "SENSEX": "in%3BSESN",
        "NIFTY IT": "in%3NNIFTYIT",
        "NIFTY FMCG": "in%3NNIFTYFMCG"
    }

    result = {}

    for name,code in indices.items():
        result[name] = get_index(code)

    return result
