from django.contrib import admin
from django.contrib.auth.models import User
from .models import AnimalInfo,AnimalColor,AnimalNews,AnimalType,CustomUser


admin.site.register(AnimalInfo)
admin.site.register(AnimalColor)
admin.site.register(AnimalNews)
admin.site.register(AnimalType)
admin.site.register(CustomUser)