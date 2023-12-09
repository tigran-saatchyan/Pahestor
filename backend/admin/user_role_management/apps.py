from django.apps import AppConfig


class UserRoleManagementConfig(AppConfig):
    """AppConfig class for the 'user_role_management' app.

    This class defines the configuration for the 'user_role_management' app.

    Attributes:
        default_auto_field (str): The default auto field to use for model
        definitions.
        name (str): The name of the app.
        verbose_name (str): The human-readable name for the app displayed in
        the admin interface.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "admin.user_role_management"
    verbose_name = "User Role Management"
