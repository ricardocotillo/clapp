from rest_framework import viewsets
from .models import Place, Booking
from .serializers import PlaceSerializer, BookingSerializer
from .filters import PlaceFilter, BookingFilter


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filterset_class = PlaceFilter


class BookingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_class = BookingFilter
