# admin.py

from django.contrib import admin

from .models import APIIntegrationLog, Notification

admin.site.register(Notification)
admin.site.register(APIIntegrationLog)
