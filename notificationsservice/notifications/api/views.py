from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from notificationsservice.notifications.api.serializers import NotificationSerializer
from notificationsservice.notifications.models import Notification


class NotificationDestroyView(DestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author__id=self.request.user.id)


class NotificationViewSet(GenericViewSet, NotificationDestroyView):
    ...
