from rest_framework.test import APITestCase
from django.shortcuts import reverse
from django.conf import settings
from django.utils import timezone

class TestApiPetfinder(APITestCase):


    data = {'username': 'gil', 'password': 'gilsander1861'}

    def authorize(self):
        token_request = self.client.post(reverse('token'), data=self.data)
        print(token_request)
        token = token_request.json().get('token')
        print(token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def test_animal_news_view(self):
        url=reverse('news')
        news = {'url_news': 'https://russian.rt.com/tag/zhivotnye',
                'description_news': 'Новость рабочая',
                'heading': 'Шок! вышла рабочая новость',
                'main_text': 'Еще больше Шока,Это новость прошла тест',
                'url_media': 'https://russian.rt.com/tag/zhivotnye',
                'time_post': str(timezone.now()),
                'gallery_img': ['https://russian.rt.com/tag/zhivotnye']}
        response=self.client.post(url,data=news)
        data = response.json()
        self.assertEqual(response.status_code, 401)
        self.authorize()
        response=self.client.get(url,data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['is_superuser'], True)