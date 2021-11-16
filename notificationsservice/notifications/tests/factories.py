from datetime import timedelta

from django.utils import timezone
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from notificationsservice.notifications.models import Notification
from notificationsservice.users.tests.factories import UserFactory


class NotificationFactory(DjangoModelFactory):

    title = Faker("sentence")
    planned_at = timezone.now() + timedelta(days=1)
    author = SubFactory(UserFactory)

    class Meta:
        model = Notification
        django_get_or_create = ("title",)
