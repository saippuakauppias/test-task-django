from django.views.generic import DetailView, ListView

from notificationsservice.notifications.models import Notification


class NotificationDetailView(DetailView):

    model = Notification
    slug_field = "pk"
    slug_url_kwarg = "id"


class NotificationListView(ListView):

    model = Notification
