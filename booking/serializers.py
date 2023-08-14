from rest_framework import serializers
from .models import Place, Court, Booking


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    courts = CourtSerializer(many=True)

    class Meta:
        model = Place
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
