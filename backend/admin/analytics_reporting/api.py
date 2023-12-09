from rest_framework import generics

from .models import InventoryReport, SalesReport
from .serializers import InventoryReportSerializer, SalesReportSerializer


class SalesReportList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Sales Reports.

    This view allows listing all Sales Reports and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of SalesReport objects.
        serializer_class (Serializer): The serializer class for SalesReport
        objects.
    """

    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer


class SalesReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Sales Report.

    This view allows retrieving, updating, and deleting a specific Sales
    Report.

    Attributes:
        queryset (QuerySet): The queryset of SalesReport objects.
        serializer_class (Serializer): The serializer class for SalesReport
        objects.
    """

    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer


class InventoryReportList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Inventory Reports.

    This view allows listing all Inventory Reports and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of InventoryReport objects.
        serializer_class (Serializer): The serializer class for
        InventoryReport objects.
    """

    queryset = InventoryReport.objects.all()
    serializer_class = InventoryReportSerializer


class InventoryReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting an Inventory Report.

    This view allows retrieving, updating, and deleting a specific Inventory
    Report.

    Attributes:
        queryset (QuerySet): The queryset of InventoryReport objects.
        serializer_class (Serializer): The serializer class for
        InventoryReport objects.
    """

    queryset = InventoryReport.objects.all()
    serializer_class = InventoryReportSerializer
