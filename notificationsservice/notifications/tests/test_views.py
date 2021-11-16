import pytest
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import reverse

from notificationsservice.notifications.models import Notification
from notificationsservice.notifications.views import NotificationOwnListView
from notificationsservice.users.models import User
from notificationsservice.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestNotificationOwnListView:
    def test_authenticated(
        self, user: User, notification: Notification, rf: RequestFactory
    ):
        request = rf.get("/notifcations/own/")
        request.user = UserFactory()
        notification.author = request.user
        notification.save()

        response = NotificationOwnListView.as_view()(request)

        assert response.status_code == 200

    def test_not_authenticated(self, user: User, rf: RequestFactory):
        request = rf.get("/notifcations/own/")
        request.user = AnonymousUser()

        response = NotificationOwnListView.as_view()(request)
        login_url = reverse(settings.LOGIN_URL)

        assert response.status_code == 302
        assert response.url == f"{login_url}?next=/notifcations/own/"
