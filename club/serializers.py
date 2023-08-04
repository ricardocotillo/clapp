from rest_framework import serializers
from django.templatetags.static import static
from .models import Club, Sport, ClubImage


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class ClubImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubImage
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    images = ClubImageSerializer(many=True)
    members_count = serializers.IntegerField()
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Club
        exclude = ('members',)

    def get_logo(self, obj: Club):
        url = obj.logo.url\
            if obj.logo\
            else static('club/img/empty.jpg')

        return self.context.get('request').build_absolute_uri(url)
