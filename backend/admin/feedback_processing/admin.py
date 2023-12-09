# admin.py

from django.contrib import admin

from .models import FeedbackAnalysis, ProductReview

admin.site.register(ProductReview)
admin.site.register(FeedbackAnalysis)
