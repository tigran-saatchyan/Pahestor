from typing import ClassVar

from rest_framework import serializers

from .models import Marketplace, MarketplaceProductLink, Order


class MarketplaceSerializer(serializers.ModelSerializer):
    """Serializer for Marketplace model.

    This serializer is used to convert Marketplace model instances into JSON
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
        model = Marketplace
        fields: ClassVar[list[str]] = [
            "id",
            "name",
            "api_key",
            "api_secret",
            "configuration",
        ]


class MarketplaceProductLinkSerializer(serializers.ModelSerializer):
    """Serializer for MarketplaceProductLink model.

    This serializer is used to convert MarketplaceProductLink model
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
        model = MarketplaceProductLink
        fields: ClassVar[list[str]] = [
            "id",
            "product",
            "marketplace",
            "external_id",
        ]


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model.

    This serializer is used to convert Order model instances into JSON format
    for API responses.

    Attributes:
        Meta (ClassVar): Configuration options for the serializer.

    Meta Attributes:
        model (Model): The model class that this serializer is associated with.
        fields (ClassVar[list[str]]): A list of fields to include in the
        serialized representation.
    """

    class Meta:
        model = Order
        fields: ClassVar[list[str]] = [
            "id",
            "marketplace",
            "external_order_id",
            "products",
            "status",
            "order_date",
            "shipment_date",
        ]
