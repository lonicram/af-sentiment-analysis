from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize


def analyze_sentence(sentence: str):
    """Analyzes sentence by using Vader sentinent analyzer.
    Tokenizes input sentence and returns its score dictioanary.

    Arguments:
        sentence (str): sentence to be analyzed
    Returns:
        dictionary containing results from Vader analyzer
    """
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    return ss


def get_overall_sentiment_from_scores(score: dict):
    """Return overall sentiment basing on scores retrieved from Vader"""
    overall_sentiment = "neutral"
    if score["compound"] >= 0.1:
        overall_sentiment = "positive"
    elif score["compound"] <= -0.1:
        overall_sentiment = "negative"

    return overall_sentiment


if __name__ == "__main__":
    while True:
        user_sentence = input("Provide sentence to be analyzed: ")
        score = analyze_sentence(user_sentence)
        overall_result = get_overall_sentiment_from_scores(score)
        print(score)
        print(f"Overally it's {overall_result} sentence.")
        if input("Do you want to continue?[y/n]: ").lower() != "y":
            break
