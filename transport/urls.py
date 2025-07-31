from django.urls import path
from .views import TransportListView, TransportCreateView


urlpatterns = [
    path('', TransportListView.as_view(), name='transport-list'),
    path('create/', TransportCreateView.as_view(), name='transport-create'),
]
