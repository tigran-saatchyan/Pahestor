# urls.py (в каталоге приложения logistics)

from django.urls import path

from . import api

app_name = "admin.logistics"

urlpatterns = [
    path("shipments/", api.ShipmentList.as_view()),
    path("shipments/<int:pk>/", api.ShipmentDetail.as_view()),
    path("providers/", api.TransportationProviderList.as_view()),
    path("providers/<int:pk>/", api.TransportationProviderDetail.as_view()),
]
