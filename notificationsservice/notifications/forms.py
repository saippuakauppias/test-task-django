from django.forms import ModelForm

from notificationsservice.notifications.models import Notification


class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = [
            "title",
            "description",
            "place",
            "author",
            "users",
            "planned_at",
            "is_completed",
        ]
