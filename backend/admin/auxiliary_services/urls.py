# urls.py (в каталоге приложения auxiliary_services)

from django.urls import path

from . import api

app_name = "admin.auxiliary_services"

urlpatterns = [
    path("notifications/", api.NotificationList.as_view()),
    path("notifications/<int:pk>/", api.NotificationDetail.as_view()),
    path("logs/", api.APIIntegrationLogList.as_view()),
    path("logs/<int:pk>/", api.APIIntegrationLogDetail.as_view()),
]
