from rest_framework import serializers
from djoser.serializers import UserSerializer as DjoserUserSerializer
from django.templatetags.static import static
from match.models import MatchClubUser
from .models import User


class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    matches_assisted = serializers.SerializerMethodField()
    matches_abandoned = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'image',
            'email',
            'first_name',
            'last_name',
            'matches_assisted',
            'matches_abandoned',
        )

    def get_image(self, obj: User):
        url = obj.image.url\
            if obj.image\
            else static('authentication/img/profile.jpg')

        return self.context.get('request').build_absolute_uri(url)

    def get_matches_abandoned(self, obj: User):
        return MatchClubUser.objects.filter(user=obj, assisted=False).count()

    def get_matches_assisted(self, obj: User):
        return MatchClubUser.objects.filter(user=obj, assisted=True).count()


class MeSerializer(DjoserUserSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'] = serializers.SerializerMethodField()
        self.fields['matches_assisted'] = serializers.SerializerMethodField()
        self.fields['matches_abandoned'] = serializers.SerializerMethodField()

    def get_image(self, obj: User):
        url = obj.image.url\
            if obj.image\
            else static('authentication/img/profile.jpg')

        return self.context.get('request').build_absolute_uri(url)

    def get_matches_abandoned(self, obj: User):
        return MatchClubUser.objects.filter(user=obj, assisted=False).count()

    def get_matches_assisted(self, obj: User):
        return MatchClubUser.objects.filter(user=obj, assisted=True).count()


class RelatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'image',
        )
