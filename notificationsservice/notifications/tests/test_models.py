import pytest

from notificationsservice.notifications.models import Notification

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(notification: Notification):
    assert notification.get_absolute_url() == f"/notifications/{notification.pk}/"
