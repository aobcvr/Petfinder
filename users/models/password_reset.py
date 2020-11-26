from django.db import models


class PasswordReset(models.Model):
    """
    Модель для смены пароля, для смены пароля обязателен подтвержденный email
    """
    user = models.ForeignKey('listanimal.CustomUser', on_delete=models.PROTECT)
    key = models.CharField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
