"""Emotion detection using IBM Watson NLP."""

import requests


def emotion_detector(text_to_analyse):
    """Analyze text and return emotion scores."""
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    payload = {"raw_document": {"text": text_to_analyse}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=payload, headers=headers, timeout=30)
    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}

    response.raise_for_status()
    result = response.json()
    emotions = result["emotionPredictions"][0]["emotion"]
    dominant = max(emotions, key=emotions.get)
    return {
        "anger": emotions.get("anger"),
        "disgust": emotions.get("disgust"),
        "fear": emotions.get("fear"),
        "joy": emotions.get("joy"),
        "sadness": emotions.get("sadness"),
        "dominant_emotion": dominant,
    }
