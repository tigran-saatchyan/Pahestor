# urls.py (в каталоге приложения feedback_processing)

from django.urls import path

from . import api

app_name = "admin.feedback_processing"

urlpatterns = [
    path("reviews/", api.ProductReviewList.as_view()),
    path("reviews/<int:pk>/", api.ProductReviewDetail.as_view()),
    path("feedbacks/", api.FeedbackAnalysisList.as_view()),
    path("feedbacks/<int:pk>/", api.FeedbackAnalysisDetail.as_view()),
]
