from rest_framework import viewsets
from .models import Place, Booking, Court
from .serializers import PlaceSerializer, BookingSerializer, CourtSerializer
from .filters import PlaceFilter, BookingFilter


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.order_by('-id')
    serializer_class = PlaceSerializer
    filterset_class = PlaceFilter


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_class = BookingFilter


class CourtViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Court.objects.order_by('-id')
    serializer_class = CourtSerializer
