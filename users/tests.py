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
    user_data = {'username': 'gil', 'password': 'gil'}

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

    @patch('users.serializer.email_auth.EmailAuthSerialazer.send_mail_auth')
    def test_email_auth(self, mock_send_mail_auth,):
        token_request = self.client.post(reverse('token'), data=self.user_data)
        token = token_request.json().get('token')
        url = reverse('email_auth')
        key = 'NoRealKey'
        email = "no-real@gmail.com"
        user = CustomUser.objects.get(username='gil')
        email_ask = EmailAuthAsk.objects.create(user=user, key=key,
                                    email_e=email)
        mock_send_mail_auth.return_value = email_ask
        response = self.client.post(url, data={'password':'gil'}, HTTP_AUTHORIZATION='Token ' + token)
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url+'?key={}'.format(key))
        self.assertEqual(response.status_code, 200)

    @patch('users.views.reset_password.PasswordResetView.send_mail_reset_password')
    def test_reset_password(self, mock_send_mail_reset_password):
        token_request = self.client.post(reverse('token'), data=self.user_data)
        token = token_request.json().get('token')
        url = reverse('reset_password')
        key = 'NoRealKey'
        new_password = 'NoRealPassword'
        user = CustomUser.objects.get(username='gil')
        password_reset = PasswordReset.objects.create(user=user,
                                                    key=key)
        mock_send_mail_reset_password.return_value = password_reset
        response = self.client.post(url, HTTP_AUTHORIZATION='Token ' + token)
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url+'?key={}&password={}'.format(key, new_password))
        self.assertEqual(response.status_code, 200)



