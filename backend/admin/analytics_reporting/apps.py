from django.apps import AppConfig


class AnalyticsReportingConfig(AppConfig):
    """AppConfig class for the 'analytics_reporting' app.

    This class defines the configuration for the 'analytics_reporting' app.

    Attributes:
        default_auto_field (str): The default auto field to use for model
        definitions.
        name (str): The name of the app.
        verbose_name (str): The human-readable name for the app displayed in
        the admin interface.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "admin.analytics_reporting"
    verbose_name = "Analytics Reporting"
