from typing import ClassVar

from rest_framework import serializers

from .models import Shipment, TransportationProvider


class ShipmentSerializer(serializers.ModelSerializer):
    """Serializer for Shipment model.

    This serializer is used to convert Shipment model instances into JSON
    format
    for API responses.

    Attributes:
        Meta (ClassVar): Configuration options for the serializer.

    Meta Attributes:
        model (Model): The model class that this serializer is associated with.
        fields (ClassVar[list[str]]): A list of fields to include in the
        serialized representation.
    """

    class Meta:
        model = Shipment
        fields: ClassVar[list[str]] = [
            "id",
            "order",
            "tracking_number",
            "status",
            "estimated_delivery_date",
            "actual_delivery_date",
        ]


class TransportationProviderSerializer(serializers.ModelSerializer):
    """Serializer for TransportationProvider model.

    This serializer is used to convert TransportationProvider model
    instances into JSON format
    for API responses.

    Attributes:
        Meta (ClassVar): Configuration options for the serializer.

    Meta Attributes:
        model (Model): The model class that this serializer is associated with.
        fields (ClassVar[list[str]]): A list of fields to include in the
        serialized representation.
    """

    class Meta:
        model = TransportationProvider
        fields: ClassVar[list[str]] = ["id", "name", "service_type"]
