from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        self.assertEqual(sentiment_analyzer("I love working with Python")['label'],"SENT_POSITIVE")
        self.assertEqual(sentiment_analyzer("I hate working with Pyhton")['label'],"SENT_NEGATIVE")
        self.assertEqual(sentiment_analyzer("I am neutral on Python")['label'],"SENT_NEUTRAL")

if __name__ == '__main__':
    unittest.main()