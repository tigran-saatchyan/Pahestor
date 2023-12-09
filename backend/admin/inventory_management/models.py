from django.db import models


class Category(models.Model):
    """Model for Categories.

    This model represents product categories with attributes for the name
    and description.

    Attributes:
        name (CharField): The name of the category.
        description (TextField, optional): A description of the category (
        blank and nullable).

    Methods:
        __str__(): Returns the name of the category.
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class Product(models.Model):
    """Model for Products.

    This model represents products with attributes for the name,
    description, price,
    quantity, category, image, and timestamps for creation and update.

    Attributes:
        name (CharField): The name of the product.
        description (TextField): The description of the product.
        price (DecimalField): The price of the product with a maximum of 10
        digits and 2 decimal places.
        quantity (IntegerField): The quantity of the product.
        category (ForeignKey to Category): The category to which the product
        belongs.
        image (ImageField, optional): An image representing the product (
        blank and nullable).
        created_at (DateTimeField): The timestamp when the product was created.
        updated_at (DateTimeField): The timestamp when the product was last
        updated.

    Methods:
        __str__(): Returns the name of the product.
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"


class StockRecord(models.Model):
    """Model for Stock Records.

    This model represents stock records with attributes for the associated
    product, quantity,
    transaction type, and date.

    Attributes:
        product (ForeignKey to Product): The product associated with the
        stock record.
        quantity (IntegerField): The quantity involved in the stock record.
        transaction_type (CharField): The type of the transaction (e.g.,
        'receipt', 'shipment').
        date (DateTimeField): The timestamp when the stock record was created.

    Methods:
        __str__(): Returns a human-readable string representation of the
        stock record.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="stock_records"
    )
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.transaction_type}"

    class Meta:
        verbose_name_plural = "Stock Records"
        verbose_name = "Stock Record"
