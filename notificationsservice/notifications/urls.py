from django.urls import path

from notificationsservice.notifications.views import (
    NotificationCreateView,
    NotificationDetailView,
    NotificationListView,
    NotificationOwnListView,
    NotificationUpdateView,
)

app_name = "notifications"
urlpatterns = [
    path("", view=NotificationListView.as_view(), name="list"),
    path("add/", view=NotificationCreateView.as_view(), name="add"),
    path("own/", view=NotificationOwnListView.as_view(), name="own"),
    path("invited/", view=NotificationOwnListView.as_view(), name="invited"),
    path("<int:id>/", view=NotificationDetailView.as_view(), name="detail"),
    path("edit/<int:pk>/", view=NotificationUpdateView.as_view(), name="edit"),
]
