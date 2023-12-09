from django.db import models

from ..marketplace_integration.models import Order


class Shipment(models.Model):
    """Model for Shipments.

    This model represents shipments with attributes for the associated order,
    tracking number, status, estimated delivery date, and actual delivery date.

    Attributes:
        order (ForeignKey to Order): The order associated with the shipment.
        tracking_number (CharField): The tracking number of the shipment.
        status (CharField): The status of the shipment (e.g., 'in transit',
        'delivered').
        estimated_delivery_date (DateTimeField, optional): The estimated
        delivery date (blank and nullable).
        actual_delivery_date (DateTimeField, optional): The actual delivery
        date (blank and nullable).

    Methods:
        __str__(): Returns a human-readable string representation of the
        shipment.
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    estimated_delivery_date = models.DateTimeField(blank=True, null=True)
    actual_delivery_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.order.external_order_id} - {self.tracking_number}"

    class Meta:
        verbose_name_plural = "Shipments"
        verbose_name = "Shipment"


class TransportationProvider(models.Model):
    """Model for Transportation Providers.

    This model represents transportation providers with attributes for the name
    and service type.

    Attributes:
        name (CharField): The name of the transportation provider.
        service_type (CharField): The service type of the provider (e.g.,
        'standard', 'express').

    Methods:
        __str__(): Returns the name of the transportation provider.
    """

    name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Transportation Providers"
        verbose_name = "Transportation Provider"
