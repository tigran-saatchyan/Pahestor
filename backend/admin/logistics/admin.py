# admin.py

from django.contrib import admin

from .models import Shipment, TransportationProvider

admin.site.register(Shipment)
admin.site.register(TransportationProvider)
