from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from config import celery_app
from notificationsservice.notifications.models import Notification
from notificationsservice.notifications.tasks import send_notification


@receiver(post_save, sender=Notification)
def notification_save(sender, instance, created, **kwargs):
    send_notification.apply_async(
        (instance.pk,), task_id=f"notify_{instance.pk}", eta=instance.planned_at
    )


@receiver(pre_delete, sender=Notification)
def notification_delete(sender, instance, **kwargs):
    celery_app.control.revoke(f"notify_{instance.pk}", terminate=True)
