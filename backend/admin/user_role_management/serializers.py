from typing import ClassVar

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Role, UserProfile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model.

    This serializer is used to convert User model instances into JSON format
    for API responses.

    Attributes:
        Meta (ClassVar): Configuration options for the serializer.

    Meta Attributes:
        model (Model): The model class that this serializer is associated with.
        fields (ClassVar[list[str]]): A list of fields to include in the
        serialized representation.
    """

    class Meta:
        model = User
        fields: ClassVar[list[str]] = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile model.

    This serializer is used to convert UserProfile model instances into JSON
    format for API responses.

    Attributes:
        user (UserSerializer): Serializer for the User associated with the
        UserProfile.

    Attributes:
        Meta (ClassVar): Configuration options for the serializer.

    Meta Attributes:
        model (Model): The model class that this serializer is associated with.
        fields (ClassVar[list[str]]): A list of fields to include in the
        serialized representation.
    """

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields: ClassVar[list[str]] = [
            "id",
            "user",
            "phone_number",
            "address",
            "role",
        ]


class RoleSerializer(serializers.ModelSerializer):
    """Serializer for Role model.

    This serializer is used to convert Role model instances into JSON format
    for API responses.

    Attributes:
        Meta (ClassVar): Configuration options for the serializer.

    Meta Attributes:
        model (Model): The model class that this serializer is associated with.
        fields (ClassVar[list[str]]): A list of fields to include in the
        serialized representation.
    """

    class Meta:
        model = Role
        fields: ClassVar[list[str]] = ["id", "name", "permissions"]
