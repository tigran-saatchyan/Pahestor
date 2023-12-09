# urls.py (в каталоге приложения inventory_management)

from django.urls import path

from . import api

app_name = "admin.inventory_management"

urlpatterns = [
    path("products/", api.ProductList.as_view()),
    path("products/<int:pk>/", api.ProductDetail.as_view()),
    path("categories/", api.CategoryList.as_view()),
    path("categories/<int:pk>/", api.CategoryDetail.as_view()),
    path("stock-records/", api.StockRecordList.as_view()),
    path("stock-records/<int:pk>/", api.StockRecordDetail.as_view()),
]
