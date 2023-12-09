from rest_framework import generics

from .models import APIIntegrationLog, Notification
from .serializers import APIIntegrationLogSerializer, NotificationSerializer


class NotificationList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Notifications.

    This view allows listing all Notifications and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of Notification objects.
        serializer_class (Serializer): The serializer class for Notification
        objects.
    """

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Notification.

    This view allows retrieving, updating, and deleting a specific
    Notification.

    Attributes:
        queryset (QuerySet): The queryset of Notification objects.
        serializer_class (Serializer): The serializer class for Notification
        objects.
    """

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class APIIntegrationLogList(generics.ListCreateAPIView):
    """API endpoint for listing and creating API Integration Logs.

    This view allows listing all API Integration Logs and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of APIIntegrationLog objects.
        serializer_class (Serializer): The serializer class for
        APIIntegrationLog objects.
    """

    queryset = APIIntegrationLog.objects.all()
    serializer_class = APIIntegrationLogSerializer


class APIIntegrationLogDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting an API
    Integration Log.

    This view allows retrieving, updating, and deleting a specific API
    Integration Log.

    Attributes:
        queryset (QuerySet): The queryset of APIIntegrationLog objects.
        serializer_class (Serializer): The serializer class for
        APIIntegrationLog objects.
    """

    queryset = APIIntegrationLog.objects.all()
    serializer_class = APIIntegrationLogSerializer
