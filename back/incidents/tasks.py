import requests
from incidents.models import Uptime, Site
from datetime import datetime, timedelta
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError, Timeout
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .serializers import SiteSerializer
from celery.schedules import crontab
from celery.task import periodic_task
from django.conf import settings
from django.core.mail import send_mail
from incidents.models import Uptime, Site
from users.models import User


@periodic_task(run_every=(crontab(minute='*')),
               name="update_to_visitor",
               ignore_result=False)
def update_to_visitor():

    sites = Site.objects.all()
    for site in sites:
        try:
            r = requests.head(site.url, timeout=4)
            Uptime.objects.create(site=site, status='up', response_time=int(
                r.elapsed.total_seconds()*1000), date=datetime.now())
        except Timeout as e:
            if not Uptime.objects.filter(status='issue',
                                         site=site,
                                         date__gte=datetime.now() -
                                         timedelta(minutes=10)).exists():
                emails = [x.email
                          for x in User.objects.all()
                          if x.send_email_for_issues]
                send_mail("We just had a time out",
                          "Please check our website, we might have issues. \
                              https: //status.djangowaves.com",
                          settings.DEFAULT_FROM_EMAIL, emails,
                          fail_silently=True)
            Uptime.objects.create(site=site, status='issue',
                                  response_time=4000, date=datetime.now())
        except Exception as e:
            if not Uptime.objects.filter(status='down',
                                         site=site,
                                         date__gte=datetime.now() -
                                         timedelta(minutes=10)).exists():
                emails = [x.email for x in User.objects.all()
                          if x.send_email_for_downtime]
                send_mail("A site has issues.",
                          "Please check our website, we might have some serious \
                              problems. https: //status.djangowaves.com",
                          settings.DEFAULT_FROM_EMAIL, emails)
            Uptime.objects.create(site=site, status='down',
                                  response_time=0, date=datetime.now())

        serializer = SiteSerializer(site)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'All',
            {'type': 'chat_message',
             'message': serializer.data}
        )
