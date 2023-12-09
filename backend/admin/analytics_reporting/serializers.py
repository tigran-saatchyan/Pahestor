from typing import ClassVar

from rest_framework import serializers

from .models import InventoryReport, SalesReport


class SalesReportSerializer(serializers.ModelSerializer):
    """Serializer for SalesReport model.

    This serializer is used to convert SalesReport model instances into JSON
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
        model = SalesReport
        fields: ClassVar[list[str]] = [
            "id",
            "date",
            "total_sales",
            "total_orders",
        ]


class InventoryReportSerializer(serializers.ModelSerializer):
    """Serializer for InventoryReport model.

    This serializer is used to convert InventoryReport model instances into
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
        model = InventoryReport
        fields: ClassVar[list[str]] = [
            "id",
            "date",
            "product",
            "starting_inventory",
            "ending_inventory",
        ]
