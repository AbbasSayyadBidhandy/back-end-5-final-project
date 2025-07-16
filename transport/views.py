from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Transport
from .serializers import TransportSerializer


class TransportListView(generics.ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
