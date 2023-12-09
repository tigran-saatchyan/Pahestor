"""Main URL Configuration"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("inventory/", include("admin.inventory_management.urls")),
    path("marketplace/", include("admin.marketplace_integration.urls")),
    path("logistics/", include("admin.logistics.urls")),
    path("analytics/", include("admin.analytics_reporting.urls")),
    path("users/", include("admin.user_role_management.urls")),
    path("feedback/", include("admin.feedback_processing.urls")),
    path("services/", include("admin.auxiliary_services.urls")),
    path("", include("docs")),
]
