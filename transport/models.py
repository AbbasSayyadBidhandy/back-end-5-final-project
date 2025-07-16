from django.db import models


class Transport(models.Model):
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flight_number = models.CharField(max_length=20, unique=True)
    total_seats = models.PositiveIntegerField(default=50)

    def __str__(self):
        return f"{self.flight_number} | \"{self.departure_city}\" to \"{self.arrival_city}\""
