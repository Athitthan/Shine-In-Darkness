from __future__ import absolute_import
import os
import time
from celery import Celery
from django.conf import settings


os.environ.setdefault('FORKED_BY_MULTIPROCESSING','1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','socialnetwork.settings')
app = Celery('socialnetwork', broker='redis://localhost/',backend='redis://localhost/')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()