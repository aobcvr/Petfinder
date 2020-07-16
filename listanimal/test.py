from django.test import TestCase
from .parseranimal import RtNewsAnimalParser

class NewsTest(TestCase):

    def test_news(self):
        news = RtNewsAnimalParser.rt_news_animal()
        if news == list:
            self.assertEqual(news.speak(), 'parser work')

    