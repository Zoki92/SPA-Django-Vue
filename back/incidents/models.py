from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
import uuid

UPTIME_STATUS_CHOICES = (
    ('up', 'All is good'),
    ('issue', 'We are having some issues'),
    ('down', 'Our website is down')
)
UPDATE_STATUS_CHOICES = (
    ('identified', 'Identified'),
    ('investigating', 'Investigating'),
    ('monitoring', 'Monitoring'),
    ('resolved', 'Resolved')
)


class Site(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def last_30_uptime_items(self):
        return self.uptime_set.all().order_by("date")[:30]

    def last_7_days_incident_items(self):
        date_today = datetime.now().replace(
            hour=0, minute=0, second=0) + timedelta(days=1)
        date_seven_days_ago = date_today - timedelta(days=7)
        return self.incident_set.all().filter(
            start__gte=date_seven_days_ago,
            start__lte=date_today
        )


class Incident(models.Model):
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True)
    solved = models.BooleanField(default=False)


def __str__(self):
    return self.title


class Uptime(models.Model):

    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    response_time = models.IntegerField()  # in seconds
    status = models.CharField(max_length=10,
                              choices=UPTIME_STATUS_CHOICES)

    def __str__(self):
        return str(self.response_time)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True,
                             default=None,
                             on_delete=models.SET_NULL)
    incident = models.ForeignKey('Incident',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 default=None)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,
                              choices=UPDATE_STATUS_CHOICES)

    def __str__(self):
        return self.incident.title + ' - ' + self.description[:20]


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    unique_id = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.email
