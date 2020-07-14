from django.contrib import admin
from django.contrib.auth.models import User
from . models_animals import AnimalInfo,AnimalColor,AnimalType
from .models import CustomUser
from . models_news import AnimalNews


admin.site.register(AnimalInfo)
admin.site.register(AnimalColor)
admin.site.register(AnimalNews)
admin.site.register(AnimalType)
admin.site.register(CustomUser)