# Emotion Detection Application

Python and Flask application for emotion detection using IBM Watson NLP.

## Project files

- `emotion_detection.py` — Watson NLP emotion detector
- `EmotionDetection/__init__.py` — package initializer
- `test_emotion_detection.py` — unit tests
- `server.py` — Flask web application

## Run

```bash
pip install flask requests
python server.py
```

The application exposes `/emotionDetector` and returns JSON emotion scores.

## Original exercise
This repository is used for the IBM Watson NLP emotion detection application exercise.
