from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Transport
from .serializers import TransportSerializer


class TransportListView(generics.ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['departure_city', 'arrival_city', 'departure_datetime', 'price']
    ordering_fields = ['price', 'departure_datetime']
