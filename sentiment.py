def calculate_sentiment(indices):

    positive = 0
    negative = 0

    for i in indices.values():

        if i["change"] > 0:
            positive += 1
        else:
            negative += 1

    if positive > negative:
        return "Bullish"

    if negative > positive:
        return "Bearish"

    return "Neutral"
