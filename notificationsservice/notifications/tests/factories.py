from datetime import timedelta

from django.db.models.signals import post_save, pre_delete
from django.utils import timezone
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from notificationsservice.notifications.models import Notification
from notificationsservice.notifications.signals import (
    notification_delete,
    notification_save,
)
from notificationsservice.users.tests.factories import UserFactory


class NotificationFactory(DjangoModelFactory):

    title = Faker("sentence")
    planned_at = timezone.now() + timedelta(days=1)
    author = SubFactory(UserFactory)

    class Meta:
        model = Notification
        django_get_or_create = ("title",)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        post_save.disconnect(notification_save, sender=model_class)
        pre_delete.disconnect(notification_delete, sender=model_class)

        return super(NotificationFactory, cls)._create(model_class, *args, **kwargs)
