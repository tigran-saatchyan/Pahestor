from django.db import models

from ..inventory_management.models import Product


class Marketplace(models.Model):
    """Model for Marketplaces.

    This model represents marketplaces with attributes for the name, API key,
    API secret, and configuration.

    Attributes:
        name (CharField): The name of the marketplace.
        api_key (CharField): The API key for the marketplace.
        api_secret (CharField, optional): The API secret for the marketplace
        (blank and nullable).
        configuration (JSONField, optional): Configuration data for the
        marketplace (blank and nullable).

    Methods:
        __str__(): Returns the name of the marketplace.
    """

    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255, blank=True, null=True)
    configuration = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Marketplaces"
        verbose_name = "Marketplace"


class MarketplaceProductLink(models.Model):
    """Model for Marketplace Product Links.

    This model represents links between products and marketplaces with
    attributes
    for the associated product, marketplace, and external ID.

    Attributes:
        product (ForeignKey to Product): The product associated with the link.
        marketplace (ForeignKey to Marketplace): The marketplace associated
        with the link.
        external_id (CharField): The external ID for the link.

    Methods:
        __str__(): Returns a human-readable string representation of the link.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.marketplace.name} - {self.product.name}"

    class Meta:
        verbose_name_plural = "Marketplace Product Links"
        verbose_name = "Marketplace Product Link"


class Order(models.Model):
    """Model for Orders.

    This model represents orders with attributes for the associated
    marketplace,
    external order ID, products, status, order date, and shipment date.

    Attributes:
        marketplace (ForeignKey to Marketplace): The marketplace associated
        with the order.
        external_order_id (CharField): The external order ID for the order.
        products (ManyToManyField to Product through OrderProduct): The
        products in the order.
        status (CharField): The status of the order (e.g., 'pending',
        'shipped', 'delivered').
        order_date (DateTimeField): The date of the order.
        shipment_date (DateTimeField, optional): The date of shipment (blank
        and nullable).

    Methods:
        __str__(): Returns a human-readable string representation of the order.
    """

    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    external_order_id = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through="OrderProduct")
    status = models.CharField(max_length=50)
    order_date = models.DateTimeField()
    shipment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.marketplace.name} - Order {self.external_order_id}"

    class Meta:
        verbose_name_plural = "Orders"
        verbose_name = "Order"


class OrderProduct(models.Model):
    """Model for Order Products.

    This model represents products within orders with attributes for the
    associated
    order, product, and quantity.

    Attributes:
        order (ForeignKey to Order): The order associated with the product.
        product (ForeignKey to Product): The product within the order.
        quantity (IntegerField): The quantity of the product in the order.

    Methods:
        __str__(): Returns a human-readable string representation of the
        order product.
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order.external_order_id} - {self.product.name}"

    class Meta:
        verbose_name_plural = "Order Products"
        verbose_name = "Order Product"
