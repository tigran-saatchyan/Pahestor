# urls.py (в каталоге приложения analytics_reporting)

from django.urls import path

from . import api

app_name = "admin.analytics_reporting"

urlpatterns = [
    path("sales-reports/", api.SalesReportList.as_view()),
    path("sales-reports/<int:pk>/", api.SalesReportDetail.as_view()),
    path("inventory-reports/", api.InventoryReportList.as_view()),
    path("inventory-reports/<int:pk>/", api.InventoryReportDetail.as_view()),
]
