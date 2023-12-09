from django.contrib.auth.models import User
from django.db import models

from ..marketplace_integration.models import Marketplace


class Notification(models.Model):
    """Model for Notifications.

    This model represents notifications with attributes for the associated
    user,
    message, status, and creation timestamp.

    Attributes:
        user (ForeignKey to User): The user associated with the notification.
        message (TextField): The content of the notification message.
        status (CharField): The status of the notification (e.g., 'unread',
        'read').
        created_at (DateTimeField): The timestamp when the notification was
        created.

    Methods:
        __str__(): Returns a human-readable string representation of the
        notification.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"

    class Meta:
        verbose_name_plural = "Notifications"
        verbose_name = "Notification"


class APIIntegrationLog(models.Model):
    """Model for API Integration Logs.

    This model represents API integration logs with attributes for the
    associated marketplace,
    log type, message, and timestamp.

    Attributes:
        marketplace (ForeignKey to Marketplace): The marketplace associated
        with the log.
        log_type (CharField): The type of the log (e.g., 'error', 'warning',
        'info').
        message (TextField): The content of the log message.
        timestamp (DateTimeField): The timestamp when the log entry was
        created.

    Methods:
        __str__(): Returns a human-readable string representation of the API
        integration log.
    """

    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    log_type = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marketplace.name} Log"

    class Meta:
        verbose_name_plural = "API Integration Logs"
        verbose_name = "API Integration Log"
