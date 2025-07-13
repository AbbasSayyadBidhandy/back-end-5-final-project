from django.urls import path
from .views import BookingListView, BookingCreateView


urlpatterns = [
    path('', BookingListView.as_view(), name='booking-list'),
    path('create/', BookingCreateView.as_view(), name='booking-create'),
]
