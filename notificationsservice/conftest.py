import pytest

from notificationsservice.notifications.models import Notification
from notificationsservice.notifications.tests.factories import NotificationFactory
from notificationsservice.users.models import User
from notificationsservice.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def notification() -> Notification:
    return NotificationFactory()
