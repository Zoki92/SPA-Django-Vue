from django.contrib import admin
from .models import (Site, Uptime, Incident,
                     Update, Subscriber)


admin.site.register(Site)
admin.site.register(Uptime)
admin.site.register(Incident)
admin.site.register(Update)
admin.site.register(Subscriber)
