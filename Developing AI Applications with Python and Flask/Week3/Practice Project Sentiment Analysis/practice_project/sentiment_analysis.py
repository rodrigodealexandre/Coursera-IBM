import requests

def setiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    return response.text
