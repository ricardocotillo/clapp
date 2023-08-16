from django_filters import rest_framework as filters
from utils.filters import NumberInFilter
from .models import Place, Booking


class PlaceFilter(filters.FilterSet):
    sports = NumberInFilter()

    class Meta:
        model = Place
        fields = ('sports', 'name',)


class BookingFilter(filters.FilterSet):
    class Meta:
        model = Booking
        fields = ('court', 'start', 'status',)
