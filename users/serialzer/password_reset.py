from users.models import PasswordReset
from uuid import uuid4

from rest_framework import serializers

from django.core.mail import send_mail
from django.http import HttpRequest
from django.conf import settings


class PasswordResetSerialazer(serializers.ModelSerializer):
    class Meta:
        model = PasswordReset
        fields = '__all__'

    def password_reset(self, request):
        """Создание заявки смены пароля, обязателен email"""
        key = uuid4()
        send_mail('Заявка на смену пароля',
                  'Для смены пароля перейдите на 127.0.0.1:8000{}?key={}'
                  .format(HttpRequest.get_full_path(request), key),
                  settings.EMAIL_HOST_USER, [self.validated_data['email']])
        PasswordReset.objects.create(user=request.user, key=key)
