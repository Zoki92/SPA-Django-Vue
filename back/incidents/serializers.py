from rest_framework import serializers
from .models import (Site, Update, Uptime,
                     Incident, Subscriber)


class UptimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uptime
        fields = ('id', 'date', 'response_time', 'status')


class UpdateSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Update
        fields = ('id',
                  'description',
                  'status',
                  'date')


class IncidentSerializer(serializers.HyperlinkedModelSerializer):
    update_set = UpdateSerializer(many=True,
                                  read_only=True)

    class Meta:
        model = Incident
        fields = ('id',
                  'title',
                  'update_set',
                  'start',
                  'end',
                  'solved')


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    uptime_set = UptimeSerializer(many=True, read_only=True,
                                  source='last_30_uptime_items')
    incident_set = IncidentSerializer(many=True, read_only=True,
                                      source='last_7_days_incident_items')

    class Meta:
        model = Site
        fields = ('id',
                  'uptime_set',
                  'incident_set',
                  'title',
                  'url',
                  'date')


class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    def validate_email(self, value):
        if Subscriber.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError(
                "Subscriber with the same email already exists")
        return value.lower()

    class Meta:
        model = Subscriber
        fields = ('email',)
