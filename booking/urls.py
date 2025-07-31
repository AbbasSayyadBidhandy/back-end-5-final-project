from django.urls import path
from .views import BookingListView, BookingCreateView, MyBookingsView, CancelBookingView


urlpatterns = [
    path('', BookingCreateView.as_view(), name='book-ticket'),
    path('my/', MyBookingsView.as_view(), name='my-bookings'),
    path('<int:pk>/cancel/', CancelBookingView.as_view(), name='cancel-booking'),
    path('', BookingListView.as_view(), name='booking-list'),
    path('create/', BookingCreateView.as_view(), name='booking-create'),
]
