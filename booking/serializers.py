from rest_framework import serializers
from .models import Booking
from transport.models import Transport
from django.utils import timezone
from datetime import datetime



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'transport', 'seat_number', 'booking_date']
        read_only_fields = ['user', 'booking_date']

    def validate(self, data):
        user = self.context['request'].user
        transport = data['transport']
        seat_number = data['seat_number']

        if seat_number < 1 or seat_number > transport.total_seats:
            raise serializers.ValidationError(
                f"Seat number must be between 1 and {transport.total_seats}."
            )

        if transport.departure_datetime < timezone.now():
            raise serializers.ValidationError(
                "Cannot book a transport that has already departed."
            )

        if Booking.objects.filter(
            user=user,
            transport=transport, 
            seat_number=seat_number
        ).exists():
            raise serializers.ValidationError(
                f"you have already booked seat number {seat_number} on this transport."
            )

        return data
