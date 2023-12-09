# admin.py

from django.contrib import admin

from .models import Role, UserProfile

admin.site.register(UserProfile)
admin.site.register(Role)
