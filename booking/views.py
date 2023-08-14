from rest_framework import viewsets
from .models import Place, Court, Booking
from .serializers import PlaceSerializer, CourtSerializer, BookingSerializer


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class BookingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
