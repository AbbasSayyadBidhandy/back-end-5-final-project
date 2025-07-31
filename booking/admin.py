from django.contrib import admin
from .models import Booking, Passenger


admin.site.register(Passenger)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'transport', 'booking_date', 'seat_number']
    search_fields = ['user__username', 'transport__flight_number']
