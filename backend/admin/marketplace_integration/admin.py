# admin.py

from django.contrib import admin

from .models import Marketplace, MarketplaceProductLink, Order

admin.site.register(Marketplace)
admin.site.register(MarketplaceProductLink)
admin.site.register(Order)
