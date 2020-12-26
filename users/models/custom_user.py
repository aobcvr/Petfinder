from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Дает возможность выбрать приоритетные новости
    """
    favorit_animal = models.ManyToManyField('listanimal.AnimalInfo')
