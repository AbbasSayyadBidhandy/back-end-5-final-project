from rest_framework import serializers
from .models import Transport


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = [
            'id',
            'departure_city',
            'arrival_city',
            'departure_datetime',
            'arrival_datetime',
            'price',
            'flight_number',
        ]
