from rest_framework.test import APITestCase
from django.shortcuts import reverse
from django.conf import settings
from django.utils import timezone
from listanimal.models import *
import os
def get_fixtures(path=settings.FIXTURES_DIR):
    '''
    Собрать список фикстур из new_fixtures для использования (архив игнорируем)
    :param path:
    :return:
    '''
    result = []
    for name in os.listdir(path):
        obj_path = os.path.join(path, name)
        if name.endswith('.zip'):
            continue
        elif os.path.isfile(obj_path):
            files_list = [obj_path]
        else:
            files_list = get_fixtures(obj_path)
        result += files_list
    return result


class TestApiPetfinder(APITestCase):

    fixtures = get_fixtures()
    user_data = {'username': 'gil', 'password': 'gilsander1861'}

    def authorize(self):
        token_request = self.client.post(reverse('token'), data=self.user_data)
        token = token_request.json().get('token')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    def test_animal_news(self):
        url=reverse('news')
        response=self.client.get(url)
        self.assertEqual(response.status_code, 401)
        self.authorize()
        response=self.client.get(url+'?search_line=нас')
        self.assertEqual(response.status_code, 200)


    def test_advertisement_all(self):
        url='/rest/advertisement/'
        response=self.client.get(url)
        self.assertEqual(response.status_code, 401)
        self.authorize()
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_advertisement_type(self):
        url=reverse('advertisement_type')
        response=self.client.get(url)
        self.assertEqual(response.status_code, 401)
        self.authorize()
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_advertisement_color(self):
        url=reverse('advertisement_color')
        response=self.client.get(url)
        self.assertEqual(response.status_code, 401)
        self.authorize()
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_advertisement_favorit(self):
        url=reverse('advertisement_favorit')
        response=self.client.get(url)
        self.assertEqual(response.status_code, 401)
        self.authorize()
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)





