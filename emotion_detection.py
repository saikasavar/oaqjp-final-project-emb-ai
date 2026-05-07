""" This module is used for emotion detection"""
import json
import requests

def emotion_detector(text_to_analyze):
    """ the function parses the text input and outputs emotional prediction """
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjob = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myjob, headers=headers,timeout=30)
    formatted_response = json.loads(response.text)
    emotion_dict = formatted_response['emotionPredictions'][0]
    anger_score = emotion_dict['emotion']['anger']
    disgust_score = emotion_dict['emotion']['disgust']
    fear_score = emotion_dict['emotion']['fear']
    joy_score = emotion_dict['emotion']['joy']
    sadness_score = emotion_dict['emotion']['sadness']
    data = {'anger':anger_score, 'disgust':disgust_score, 'fear': fear_score, 
    'joy': joy_score, 'sadness': sadness_score }
    dominant_emotion = max(data, key=data.get)
    result = {'anger':anger_score, 'disgust':disgust_score, 'fear': fear_score, 'joy': joy_score, 
    'sadness': sadness_score, 'dominant_emotion': dominant_emotion  }
    return result
