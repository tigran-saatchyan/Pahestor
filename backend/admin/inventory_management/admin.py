# admin.py

from django.contrib import admin

from .models import Category, Product, StockRecord

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(StockRecord)
