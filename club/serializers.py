from rest_framework import serializers
from django.templatetags.static import static
from authentication.serializers import UserSerializer
from booking.serializers import CourtSerializer
from utils.serializers import SportSerializer
from .models import Club, Membership, Scrimmage, ScrimmageUser


class ClubSerializer(serializers.ModelSerializer):
    sport = SportSerializer(read_only=True)
    sport_id = serializers.IntegerField()
    # images = ClubImageSerializer(many=True, read_only=True)
    members_count = serializers.IntegerField(read_only=True)
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = (
            'id',
            'sport',
            'sport_id',
            'name',
            'logo',
            # 'images',
            'members_count',
            'created_at',
            'updated_at',
        )

    def get_logo(self, obj: Club):
        url = obj.logo.url\
            if obj.logo\
            else static('club/img/empty.jpg')

        return self.context.get('request').build_absolute_uri(url)

    def create(self, validated_data):
        club = Club.objects.create(
            owner=self.context.get('request').user,
            **validated_data
        )
        Membership.objects.create(
            club=club,
            user=self.context.get('request').user,
            role=Membership.Roles.OWNER,
        )
        club.members_count = 1
        return club


class MembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Membership
        fields = '__all__'


class ScrimmageUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ScrimmageUser
        exclude = ('scrimmage',)


class ScrimmageSerializer(serializers.ModelSerializer):
    scrimmage_users = ScrimmageUserSerializer(many=True, read_only=True)
    court = CourtSerializer(read_only=True)

    class Meta:
        model = Scrimmage
        exclude = ('club', 'users',)
