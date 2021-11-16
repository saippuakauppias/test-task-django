from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse

from config import celery_app
from notificationsservice.notifications.models import Notification


@celery_app.task()
def send_notification(nid: int, **kwargs):
    nobj = Notification.objects.get(pk=nid)
    recipients_users = [u["email"] for u in nobj.users.values("email").all()]
    recipients_all = list(set([nobj.author.email] + recipients_users))

    url = reverse("notifications:detail", kwargs={"id": nid})

    send_mail(
        subject="Notification from NS",
        message=f"{nobj.title}: {url}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients_all,
        fail_silently=False,
    )
