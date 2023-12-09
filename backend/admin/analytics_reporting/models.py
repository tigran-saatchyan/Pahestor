from django.db import models

from ..inventory_management.models import Product


class SalesReport(models.Model):
    """Model for Sales Reports.

    This model represents sales reports with attributes for date,
    total sales, and total orders.

    Attributes:
        date (DateField): The date of the sales report.
        total_sales (DecimalField): The total sales amount with a maximum of
        12 digits and 2 decimal places.
        total_orders (IntegerField): The total number of orders.

    Methods:
        __str__(): Returns a human-readable string representation of the
        sales report.
    """

    date = models.DateField()
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    total_orders = models.IntegerField()

    def __str__(self):
        return f"Sales Report {self.date}"

    class Meta:
        verbose_name_plural = "Sales Reports"
        verbose_name = "Sales Report"


class InventoryReport(models.Model):
    """Model for Inventory Reports.

    This model represents inventory reports with attributes for date,
    associated product,
    starting inventory, and ending inventory.

    Attributes:
        date (DateField): The date of the inventory report.
        product (ForeignKey to Product): The product associated with the
        inventory report.
        starting_inventory (IntegerField): The starting inventory count.
        ending_inventory (IntegerField): The ending inventory count.

    Methods:
        __str__(): Returns a human-readable string representation of the
        inventory report.
    """

    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    starting_inventory = models.IntegerField()
    ending_inventory = models.IntegerField()

    def __str__(self):
        return f"Inventory Report {self.date} - {self.product.name}"

    class Meta:
        verbose_name_plural = "Inventory Reports"
        verbose_name = "Inventory Report"
