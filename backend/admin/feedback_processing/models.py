from django.db import models

from ..inventory_management.models import Product


class ProductReview(models.Model):
    """Model for Product Reviews.

    This model represents product reviews with attributes for the associated
    product,
    rating, comment, and creation timestamp.

    Attributes:
        product (ForeignKey to Product): The product associated with the
        review.
        rating (IntegerField): The rating given in the review.
        comment (TextField): The text comment provided in the review.
        created_at (DateTimeField): The timestamp when the review was created.

    Methods:
        __str__(): Returns a human-readable string representation of the
        product review.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - Review"

    class Meta:
        verbose_name_plural = "Product Reviews"
        verbose_name = "Product Review"


class FeedbackAnalysis(models.Model):
    """Model for Feedback Analyses.

    This model represents feedback analyses with attributes for the
    associated review,
    sentiment score, and analysis timestamp.

    Attributes:
        review (ForeignKey to ProductReview): The product review associated
        with the analysis.
        sentiment_score (FloatField): The sentiment score of the review
        analysis.
        analyzed_at (DateTimeField): The timestamp when the analysis was
        performed.

    Methods:
        __str__(): Returns a human-readable string representation of the
        feedback analysis.
    """

    review = models.ForeignKey(ProductReview, on_delete=models.CASCADE)
    sentiment_score = models.FloatField()
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for Review {self.review.id}"

    class Meta:
        verbose_name_plural = "Feedback Analysis"
        verbose_name = "Feedback Analysis"
