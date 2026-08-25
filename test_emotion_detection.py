import unittest
from emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am very happy today!")
        self.assertIsNotNone(result)
        self.assertIn("dominant_emotion", result)

    def test_sadness(self):
        result = emotion_detector("I am feeling sad and unhappy.")
        self.assertIsNotNone(result)
        self.assertIn("sadness", result)

    def test_anger(self):
        result = emotion_detector("I am extremely angry.")
        self.assertIsNotNone(result)
        self.assertIn("anger", result)


if __name__ == "__main__":
    unittest.main()
