from __future__ import absolute_import

from celery import shared_task
import requests


@shared_task
def get_names():
    r = requests.get('http://api.uinames.com/?amount=25&country=Brazil')
    return r
