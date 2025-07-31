import django_filters
from .models import Transport

class TransportFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    date = django_filters.DateFilter(field_name='departure_datetime', lookup_expr='date')

    class Meta:
        model = Transport
        fields = ['departure_city', 'arrival_city', 'transport_type']
