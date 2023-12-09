from django.contrib import admin

from .models import InventoryReport, SalesReport

admin.site.register(SalesReport)
admin.site.register(InventoryReport)
