from django.contrib import admin
from .models import Transport

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure_city', 'arrival_city', 'departure_datetime', 'arrival_datetime', 'price')
    search_fields = ('flight_number', 'departure_city', 'arrival_city')
    list_filter = ('departure_city', 'arrival_city', 'departure_datetime')