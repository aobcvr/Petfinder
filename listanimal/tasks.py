from __future__ import absolute_import, unicode_literals
from datetime import timedelta
from django.core.management import call_command

from celery.task import periodic_task


@periodic_task(run_every=(timedelta(minutes=1)), name='create_news')
def check_new_news():
    """
    каждую минуту производит парсинг сайта rt_news с тэгом животные
    """
    return call_command('create_news')


@periodic_task(run_every=(timedelta(minutes=1)), name='create_animal')
def check_new_animals():
    """
    каждую минуту производит запрос на API сайта petfinder
    """
    return call_command('create_animal')
