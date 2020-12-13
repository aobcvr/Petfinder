from django.contrib import admin
from .models import EmailAuthAsk, PasswordReset, CustomUser

admin.site.register(EmailAuthAsk)
admin.site.register(PasswordReset)
admin.site.register(CustomUser)
