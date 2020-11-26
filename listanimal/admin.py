from django.contrib import admin
from .models import AnimalInfo, AnimalColor, AnimalNews, AnimalType, \
                    NewestLogFileContent, Comment, CustomUser


admin.site.register(AnimalInfo)
admin.site.register(AnimalColor)
admin.site.register(AnimalNews)
admin.site.register(AnimalType)
admin.site.register(NewestLogFileContent)
admin.site.register(Comment)
admin.site.register(CustomUser)
