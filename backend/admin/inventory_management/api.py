from rest_framework import generics

from .models import Category, Product, StockRecord
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    StockRecordSerializer,
)


class ProductList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Products.

    This view allows listing all Products and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of Product objects.
        serializer_class (Serializer): The serializer class for Product
        objects.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Product.

    This view allows retrieving, updating, and deleting a specific Product.

    Attributes:
        queryset (QuerySet): The queryset of Product objects.
        serializer_class (Serializer): The serializer class for Product
        objects.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Categories.

    This view allows listing all Categories and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of Category objects.
        serializer_class (Serializer): The serializer class for Category
        objects.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Category.

    This view allows retrieving, updating, and deleting a specific Category.

    Attributes:
        queryset (QuerySet): The queryset of Category objects.
        serializer_class (Serializer): The serializer class for Category
        objects.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StockRecordList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Stock Records.

    This view allows listing all Stock Records and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of StockRecord objects.
        serializer_class (Serializer): The serializer class for StockRecord
        objects.
    """

    queryset = StockRecord.objects.all()
    serializer_class = StockRecordSerializer


class StockRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Stock Record.

    This view allows retrieving, updating, and deleting a specific Stock
    Record.

    Attributes:
        queryset (QuerySet): The queryset of StockRecord objects.
        serializer_class (Serializer): The serializer class for StockRecord
        objects.
    """

    queryset = StockRecord.objects.all()
    serializer_class = StockRecordSerializer
