from rest_framework import serializers

from notificationsservice.notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification

        extra_kwargs = {
            "url": {"lookup_field": "pk"},
        }
