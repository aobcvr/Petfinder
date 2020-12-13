from django.shortcuts import reverse
from django.conf import settings

from users.models.custom_user import CustomUser
from users.models.email_auth_models import EmailAuthAsk
from users.models.password_reset import PasswordReset

from unittest.mock import patch
from rest_framework.test import APITestCase

import os

def get_fixtures(path=settings.FIXTURES_DIR):
    '''
    Собрать список фикстур из new_fixtures для использования
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


class TestUserApp(APITestCase):

    fixtures = get_fixtures()

    def test_registration(self):
        url = reverse('registration')
        data = {'username': 'user',
                'password': 'qazwsx1861',
                'password2': 'qazwsx1861'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        url = reverse('login')
        data = {'username': 'user',
                'password': 'qazwsx1861'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    @patch('users.views.email_auth.EmailAuth.create')
    def test_email_auth(self, mock_create,):
        url = reverse('email_auth')
        key = 'NoRealKey'
        user = CustomUser.objects.get(username='gil')
        email_ask = EmailAuthAsk.objects.create(user=user, key=key,
                                    email_e='no-real@gmail.com')
        mock_create.return_value = email_ask
        response = self.client.get(url+'?key={}'.format(key))
        self.assertEqual(response.status_code, 200)

    @patch('users.views.reset_password.PasswordResetView.create')
    def test_reset_password(self, mock_reset_password):
        url = reverse('reset_password')
        key = 'NoRealKey'
        new_password = 'NoRealPassword'
        user = CustomUser.objects.get(username='gil')
        password_ask = PasswordReset.objects.create(user=user,
                                                    key=key)
        mock_reset_password.return_value = password_ask
        response = self.client.get(url+'?key={}&password={}'.format(key, new_password))
        self.assertEqual(response.status_code, 200)



