from django.contrib import admin
from .models import EmailAuthAsk, PasswordReset

admin.site.register(EmailAuthAsk)
admin.site.register(PasswordReset)
