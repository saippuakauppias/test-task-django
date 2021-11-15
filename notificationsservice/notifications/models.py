from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from notificationsservice.users.models import User


class Notification(models.Model):

    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"))
    place = models.CharField(_("Place"), max_length=50)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    planned_at = models.DateTimeField(_("Planned at"))
    is_completed = models.BooleanField(_("Is completed"), default=False)

    def get_absolute_url(self):
        return reverse("notifications:detail", kwargs={"id": self.pk})
