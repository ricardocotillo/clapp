from rest_framework import serializers
from authentication.serializers import UserSerializer
from .models import Club, Sport


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    members_count = serializers.IntegerField()

    class Meta:
        model = Club
        exclude = ('members',)
