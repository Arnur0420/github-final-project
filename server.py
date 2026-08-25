from flask import Flask, jsonify, request
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    text = request.args.get("text") if request.method == "GET" else request.form.get("text")
    if not text or not text.strip():
        return jsonify({"error": "Invalid input"}), 400

    result = emotion_detector(text)
    if result.get("dominant_emotion") is None:
        return jsonify({"error": "Unable to analyze input"}), 400
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
