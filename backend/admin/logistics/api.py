from rest_framework import generics

from .models import Shipment, TransportationProvider
from .serializers import ShipmentSerializer, TransportationProviderSerializer


class ShipmentList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Shipments.

    This view allows listing all Shipments and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of Shipment objects.
        serializer_class (Serializer): The serializer class for Shipment
        objects.
    """

    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ShipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Shipment.

    This view allows retrieving, updating, and deleting a specific Shipment.

    Attributes:
        queryset (QuerySet): The queryset of Shipment objects.
        serializer_class (Serializer): The serializer class for Shipment
        objects.
    """

    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class TransportationProviderList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Transportation Providers.

    This view allows listing all Transportation Providers and creating new
    ones.

    Attributes:
        queryset (QuerySet): The queryset of TransportationProvider objects.
        serializer_class (Serializer): The serializer class for
        TransportationProvider objects.
    """

    queryset = TransportationProvider.objects.all()
    serializer_class = TransportationProviderSerializer


class TransportationProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Transportation
    Provider.

    This view allows retrieving, updating, and deleting a specific
    Transportation Provider.

    Attributes:
        queryset (QuerySet): The queryset of TransportationProvider objects.
        serializer_class (Serializer): The serializer class for
        TransportationProvider objects.
    """

    queryset = TransportationProvider.objects.all()
    serializer_class = TransportationProviderSerializer
