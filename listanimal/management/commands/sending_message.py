import os
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        send_mail('subjecr','Я хз что это значит','dkdjjdkd@gmail.com',['paveligin1861@gmail.com'],
                  fail_silently=False)