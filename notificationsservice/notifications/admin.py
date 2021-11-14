from django.contrib import admin

from notificationsservice.notifications.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = ["title", "planned_at", "is_completed"]
    search_fields = ["title", "description"]
