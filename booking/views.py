from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class CancelBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            booking = Booking.objects.get(pk=pk, user=request.user)
            booking.delete()
            return Response({"message": "Booking cancelled"}, status=200)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=404)