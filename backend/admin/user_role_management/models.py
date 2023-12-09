from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    """Model for user roles.

    This model represents user roles with attributes for the role name and
    associated permissions.

    Attributes:
        name (CharField): The name of the role.
        permissions (ManyToManyField to auth.Permission): The permissions
        associated with the role.

    Methods:
        __str__(): Returns the name of the role.
    """

    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField("auth.Permission")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Roles"
        verbose_name = "Role"


class UserProfile(models.Model):
    """Model for user profiles.

    This model represents user profiles with attributes for the user,
    phone number, address, and role.

    Attributes:
        user (OneToOneField to User): The user associated with the profile.
        phone_number (CharField, optional): The phone number of the user (
        blank and nullable).
        address (TextField, optional): The address of the user (blank and
        nullable).
        role (ForeignKey to Role): The role associated with the user profile.

    Methods:
        __str__(): Returns the username of the associated user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "User Profiles"
        verbose_name = "User Profile"
