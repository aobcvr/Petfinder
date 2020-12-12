from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.core.mail import send_mail
from django.http import HttpRequest
from django.conf import settings
from users.models import PasswordReset

from uuid import uuid4


class PasswordResetView(viewsets.ViewSet):
    """
    Смена пароля производится только при подтвержденном email
    ,при наличии email отправляется заявка на смену пароля с уникальным ключем,
    заявка удаляется через 5 минут, при подтверждении заявки через почту
    отправляет на форму для указания нового пароля
    """

    @action(methods=['post'], detail=True, permission_classes=['IsAuthenticated'])
    def create(self, request):
        """
        Создает форму для смены пароля и отправляет на email сообщение
        """
        if request.user.email is '':
            return Response({"status": "email is not auth"})
        key = uuid4()
        PasswordReset.objects.create(user=request.user, key=key)
        send_mail('Заявка на смену пароля',
                  'Для смены пароля перейдите на 127.0.0.1:8000{}?key={}'
                  .format(HttpRequest.get_full_path(request), key),
                  settings.EMAIL_HOST_USER, [request.user.email])
        return Response({'status': 'check your email'})

    @action(methods=['get'], detail=True, permission_classes=['AllowAny'])
    def get(self, request):
        """
        Форма для смены пароля аккаунта, принимает
        ключ в ссылку и новый пароль
        """
        new_password = request.GET['password']
        norm_key = PasswordReset.objects.get(key=request.GET['key'])
        norm_key.user.password = new_password
        norm_key.user.save(update_fields=['password'])
        return Response({'status': 'password is changed'})
