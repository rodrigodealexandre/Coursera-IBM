"""
This module provides a function to perform sentiment analysis using
the Watson NLP Library.
"""
import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    Analyze the sentiment of the given text using Watson NLP Library.

    Args:
        text_to_analyse (str): The text to analyze.

    Returns:
        dict: The sentiment analysis result containing label and score.
    """
    url = (
        'https://sn-watson-sentiment-bert.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/SentimentPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers, timeout=10)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        return {"label": label, "score": score}
    return {"label": None, "score": None}
