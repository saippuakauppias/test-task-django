from django.urls import path

from notificationsservice.notifications.views import (
    NotificationDetailView,
    NotificationListView,
)

app_name = "notifications"
urlpatterns = [
    path("", view=NotificationListView.as_view(), name="list"),
    path("<int:id>/", view=NotificationDetailView.as_view(), name="detail"),
]
