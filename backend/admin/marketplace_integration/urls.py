# urls.py (в каталоге приложения marketplace_integration)

from django.urls import path

from . import api

app_name = "admin.marketplace_integration"

urlpatterns = [
    path("marketplaces/", api.MarketplaceList.as_view()),
    path("marketplaces/<int:pk>/", api.MarketplaceDetail.as_view()),
    path("links/", api.MarketplaceProductLinkList.as_view()),
    path("links/<int:pk>/", api.MarketplaceProductLinkDetail.as_view()),
    path("orders/", api.OrderList.as_view()),
    path("orders/<int:pk>/", api.OrderDetail.as_view()),
]
