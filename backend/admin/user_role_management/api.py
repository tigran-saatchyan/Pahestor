from rest_framework import generics

from .models import Role, UserProfile
from .serializers import RoleSerializer, UserProfileSerializer


class UserProfileList(generics.ListCreateAPIView):
    """API endpoint for listing and creating User Profiles.

    This view allows listing all User Profiles and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of UserProfile objects.
        serializer_class (Serializer): The serializer class for UserProfile
        objects.
    """

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a User Profile.

    This view allows retrieving, updating, and deleting a specific User
    Profile.

    Attributes:
        queryset (QuerySet): The queryset of UserProfile objects.
        serializer_class (Serializer): The serializer class for UserProfile
        objects.
    """

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class RoleList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Roles.

    This view allows listing all Roles and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of Role objects.
        serializer_class (Serializer): The serializer class for Role objects.
    """

    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Role.

    This view allows retrieving, updating, and deleting a specific Role.

    Attributes:
        queryset (QuerySet): The queryset of Role objects.
        serializer_class (Serializer): The serializer class for Role objects.
    """

    queryset = Role.objects.all()
    serializer_class = RoleSerializer
