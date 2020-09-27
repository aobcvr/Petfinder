from django.db import models
from django.contrib.auth.models import AbstractUser
'''
Дает возможность выбрать приоритетные новости
'''

class CustomUser(AbstractUser):
    favorit_animal = models.ManyToManyField('AnimalInfo')











