import requests

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}


def get_index(symbol):

    url = f"https://priceapi.moneycontrol.com/pricefeed/notapplicable/inidicesindia/{symbol}"

    r = requests.get(url, headers=headers, timeout=10)

    if r.status_code != 200:
        return {"price": "NA", "change": 0}

    try:
        data = r.json()["data"]

        return {
            "price": data["pricecurrent"],
            "change": float(data["pricepercentchange"])
        }

    except:
        return {"price": "NA", "change": 0}


def get_indices():

    indices = {
        "NIFTY 50": "in%3BNSEI",
        "BANK NIFTY": "in%3NNSEBANK",
        "SENSEX": "in%3BSESN",
        "NIFTY IT": "in%3NNIFTYIT",
        "NIFTY FMCG": "in%3NNIFTYFMCG"
    }

    result = {}

    for name, code in indices.items():
        result[name] = get_index(code)

    return result
