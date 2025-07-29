from django.db import models


class Booking (models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    transport = models.ForeignKey(
        'transport.Transport', on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('transport', 'seat_number')

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"
class Passenger(models.Model):
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=10)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

