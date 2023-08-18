from rest_framework import serializers
from drf_queryfields import QueryFieldsMixin
from authentication.serializers import RelatedUserSerializer
from club.serializers import SportSerializer
from feedback.serializers import ImageSerializer
from .models import Place, Court, Booking


class CourtSerializer(serializers.ModelSerializer):
    sport = SportSerializer()

    class Meta:
        model = Court
        fields = '__all__'


class PlaceSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    courts = CourtSerializer(many=True)
    owner = RelatedUserSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Place
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
