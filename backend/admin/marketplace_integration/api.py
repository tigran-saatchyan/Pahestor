from rest_framework import generics

from .models import Marketplace, MarketplaceProductLink, Order
from .serializers import (
    MarketplaceProductLinkSerializer,
    MarketplaceSerializer,
    OrderSerializer,
)


class MarketplaceList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Marketplaces.

    This view allows listing all Marketplaces and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of Marketplace objects.
        serializer_class (Serializer): The serializer class for Marketplace
        objects.
    """

    queryset = Marketplace.objects.all()
    serializer_class = MarketplaceSerializer


class MarketplaceDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Marketplace.

    This view allows retrieving, updating, and deleting a specific Marketplace.

    Attributes:
        queryset (QuerySet): The queryset of Marketplace objects.
        serializer_class (Serializer): The serializer class for Marketplace
        objects.
    """

    queryset = Marketplace.objects.all()
    serializer_class = MarketplaceSerializer


class MarketplaceProductLinkList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Marketplace Product Links.

    This view allows listing all Marketplace Product Links and creating new
    ones.

    Attributes:
        queryset (QuerySet): The queryset of MarketplaceProductLink objects.
        serializer_class (Serializer): The serializer class for
        MarketplaceProductLink objects.
    """

    queryset = MarketplaceProductLink.objects.all()
    serializer_class = MarketplaceProductLinkSerializer


class MarketplaceProductLinkDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Marketplace
    Product Link.

    This view allows retrieving, updating, and deleting a specific
    Marketplace Product Link.

    Attributes:
        queryset (QuerySet): The queryset of MarketplaceProductLink objects.
        serializer_class (Serializer): The serializer class for
        MarketplaceProductLink objects.
    """

    queryset = MarketplaceProductLink.objects.all()
    serializer_class = MarketplaceProductLinkSerializer


class OrderList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Orders.

    This view allows listing all Orders and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of Order objects.
        serializer_class (Serializer): The serializer class for Order objects.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting an Order.

    This view allows retrieving, updating, and deleting a specific Order.

    Attributes:
        queryset (QuerySet): The queryset of Order objects.
        serializer_class (Serializer): The serializer class for Order objects.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
