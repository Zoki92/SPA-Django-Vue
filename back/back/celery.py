from __future__ import absolute_import

from django.conf import settings
from celery import Celery


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')


# set the default Django settings module for the 'celery' program.
app = Celery('back')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
