from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from users.models import EmailAuthAsk
from users.models import PasswordReset


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.remove_out_auth()

    def remove_out_auth(self):
        EmailAuthAsk.objects.filter(time_create__lte=datetime.now()
                                    - timedelta(minutes=5)).delete()
        PasswordReset.objects.filter(time_create__lte=datetime.now()
                                    - timedelta(minutes=5)).delete()
