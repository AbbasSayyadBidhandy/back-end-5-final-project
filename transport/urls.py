from django.urls import path
from .views import TransportListView


urlpatterns = [
    path('', TransportListView.as_view(), name='transport-list'),
]
