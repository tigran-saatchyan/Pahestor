from rest_framework import generics

from .models import FeedbackAnalysis, ProductReview
from .serializers import FeedbackAnalysisSerializer, ProductReviewSerializer


class ProductReviewList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Product Reviews.

    This view allows listing all Product Reviews and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of ProductReview objects.
        serializer_class (Serializer): The serializer class for
        ProductReview objects.
    """

    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class ProductReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Product Review.

    This view allows retrieving, updating, and deleting a specific Product
    Review.

    Attributes:
        queryset (QuerySet): The queryset of ProductReview objects.
        serializer_class (Serializer): The serializer class for
        ProductReview objects.
    """

    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class FeedbackAnalysisList(generics.ListCreateAPIView):
    """API endpoint for listing and creating Feedback Analyses.

    This view allows listing all Feedback Analyses and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of FeedbackAnalysis objects.
        serializer_class (Serializer): The serializer class for
        FeedbackAnalysis objects.
    """

    queryset = FeedbackAnalysis.objects.all()
    serializer_class = FeedbackAnalysisSerializer


class FeedbackAnalysisDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, and deleting a Feedback Analysis.

    This view allows retrieving, updating, and deleting a specific Feedback
    Analysis.

    Attributes:
        queryset (QuerySet): The queryset of FeedbackAnalysis objects.
        serializer_class (Serializer): The serializer class for
        FeedbackAnalysis objects.
    """

    queryset = FeedbackAnalysis.objects.all()
    serializer_class = FeedbackAnalysisSerializer
