from typing import ClassVar

from rest_framework import serializers

from .models import Category, Product, StockRecord


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model.

    This serializer is used to convert Product model instances into JSON format
    for API responses.

    Attributes:
        Meta (ClassVar): Configuration options for the serializer.

    Meta Attributes:
        model (Model): The model class that this serializer is associated with.
        fields (ClassVar[list[str]]): A list of fields to include in the
        serialized representation.
    """

    class Meta:
        model = Product
        fields: ClassVar[list[str]] = [
            "id",
            "name",
            "description",
            "price",
            "quantity",
            "category",
            "image",
            "created_at",
            "updated_at",
        ]


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model.

    This serializer is used to convert Category model instances into JSON
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
        model = Category
        fields: ClassVar[list[str]] = ["id", "name", "description"]


class StockRecordSerializer(serializers.ModelSerializer):
    """Serializer for StockRecord model.

    This serializer is used to convert StockRecord model instances into JSON
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
        model = StockRecord
        fields: ClassVar[list[str]] = [
            "id",
            "product",
            "quantity",
            "transaction_type",
            "date",
        ]
