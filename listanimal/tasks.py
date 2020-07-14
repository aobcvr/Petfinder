from __future__ import absolute_import,unicode_literals
from datetime import timedelta
from django.core.management import call_command

from celery.task import periodic_task


@periodic_task(run_every=(timedelta(minutes=1)), name='createnews')
def check_new_news():
    return call_command('createnews')

@periodic_task(run_every=(timedelta(minutes=1)), name='createanimal')
def check_new_animals():
    return call_command('createanimal')
