import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    pl = { "raw_document": { "text": text_to_analyze } } 
    try:
        response = requests.post(url, json=pl, headers=headers)
        if response.status_code == 200:
            txt = json.loads(response.text)
            emotion_predictions = txt['emotionPredictions'][0]['emotion']
            anger_score = emotion_predictions['anger']
            disgust_score = emotion_predictions['disgust']
            fear_score = emotion_predictions['fear']
            joy_score = emotion_predictions['joy']
            sadness_score = emotion_predictions['sadness']
            dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
            result = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
            return result
        else:
            return {"error": f"Server returned status code {response.status_code}"}
    except (requests.exceptions.RequestException, KeyError, IndexError, json.JSONDecodeError) as e:
        return {"error": f"An error occurred while processing the request: {str(e)}"}