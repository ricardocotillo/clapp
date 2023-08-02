from django.templatetags.static import static
from rest_framework import serializers
from djoser.serializers import UserSerializer as DjoserUserSerializer
from django.utils.functional import cached_property
from match.models import MatchPlayer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'image', 'email', 'first_name', 'last_name',)

    def get_image(self, obj: User):
        return obj.image.url if obj.image else static('authentication/img/profile.jpg')


class MeSerializer(DjoserUserSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'] = serializers.SerializerMethodField()
        self.fields['rating'] = serializers.FloatField()
        # self.fields['matches_assisted'] = serializers.IntegerField()
        # self.fields['matches_abandoned'] = serializers.IntegerField()

    def get_image(self, obj: User):
        url = obj.image.url\
            if obj.image\
            else static('authentication/img/profile.jpg')

        return self.context.get('request').build_absolute_uri(url)
