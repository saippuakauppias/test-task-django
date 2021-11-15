from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView

from notificationsservice.notifications.forms import NotificationForm
from notificationsservice.notifications.models import Notification


class NotificationDetailView(DetailView):

    model = Notification
    slug_field = "pk"
    slug_url_kwarg = "id"


class NotificationListView(ListView):

    model = Notification


class NotificationOwnListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Notification.objects.filter(author__id=self.request.user.id).all()


class NotificationInvitedListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Notification.objects.filter(users=self.request.user.id).all()


class NotificationUpdateView(LoginRequiredMixin, UpdateView):

    form_class = NotificationForm

    def get_object(self):
        return Notification.objects.get(pk=self.kwargs["pk"])
