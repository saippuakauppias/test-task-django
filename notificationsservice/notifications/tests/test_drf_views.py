import pytest
from django.test import RequestFactory

from notificationsservice.notifications.api.views import NotificationViewSet
from notificationsservice.notifications.models import Notification
from notificationsservice.users.models import User

pytestmark = pytest.mark.django_db


class TestNotificationViewSet:
    def test_get_queryset(
        self, user: User, notification: Notification, rf: RequestFactory
    ):
        view = NotificationViewSet()
        request = rf.get("/api-url/")
        request.user = user

        view.request = request

        notification.author = user
        notification.save()

        assert notification in view.get_queryset()

    def test_get_queryset__with_another_author(
        self, user: User, notification: Notification, rf: RequestFactory
    ):
        view = NotificationViewSet()
        request = rf.get("/api-url/")
        request.user = user

        view.request = request

        assert notification not in view.get_queryset()
