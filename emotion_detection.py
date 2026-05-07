""" This module is used for emotion detection"""
import requests

def emotion_detector(text_to_analyze):
    """ the function parses the text input and outputs emotional prediction """
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjob = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myjob, headers=headers,timeout=10)
    return response.text
