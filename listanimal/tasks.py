from __future__ import absolute_import,unicode_literals
from celery import shared_task
from datetime import timedelta
from django.core.management import call_command

from celery.task import periodic_task
from celery.schedules import crontab


@periodic_task(run_every=(timedelta(hours=1)), name='createnews')
def chck_new_news():
    return call_command('createnews')

@periodic_task(run_every=(timedelta(hours=1)), name='createanimal')
def check_new_animals():
    return call_command('createanimal')
