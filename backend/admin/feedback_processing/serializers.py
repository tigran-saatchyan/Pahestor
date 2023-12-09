from typing import ClassVar

from rest_framework import serializers

from .models import FeedbackAnalysis, ProductReview


class ProductReviewSerializer(serializers.ModelSerializer):
    """Serializer for ProductReview model.

    This serializer is used to convert ProductReview model instances into
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
        model = ProductReview
        fields: ClassVar[list[str]] = [
            "id",
            "product",
            "rating",
            "comment",
            "created_at",
        ]


class FeedbackAnalysisSerializer(serializers.ModelSerializer):
    """Serializer for FeedbackAnalysis model.

    This serializer is used to convert FeedbackAnalysis model instances into
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
        model = FeedbackAnalysis
        fields: ClassVar[list[str]] = [
            "id",
            "review",
            "sentiment_score",
            "analyzed_at",
        ]
