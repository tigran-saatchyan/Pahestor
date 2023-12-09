from typing import ClassVar

from rest_framework import serializers

from .models import APIIntegrationLog, Notification


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer for Notification model.

    This serializer is used to convert Notification model instances into
    JSON format
    for API responses.

    Attributes:
        Meta (ClassVar): Configuration options for the serializer.

    Meta Attributes:
        model (Model): The model class that this serializer is associated with.
        fields (ClassVar[list[str]]): A list of fields to include in the
        serialized representation.
    """

    class Meta:
        model = Notification
        fields: ClassVar[list[str]] = [
            "id",
            "user",
            "message",
            "status",
            "created_at",
        ]


class APIIntegrationLogSerializer(serializers.ModelSerializer):
    """Serializer for APIIntegrationLog model.

    This serializer is used to convert APIIntegrationLog model instances
    into JSON format
    for API responses.

    Attributes:
        Meta (ClassVar): Configuration options for the serializer.

    Meta Attributes:
        model (Model): The model class that this serializer is associated with.
        fields (ClassVar[list[str]]): A list of fields to include in the
        serialized representation.
    """

    class Meta:
        model = APIIntegrationLog
        fields: ClassVar[list[str]] = [
            "id",
            "marketplace",
            "log_type",
            "message",
            "timestamp",
        ]
