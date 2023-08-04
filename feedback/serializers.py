from rest_framework import serializers
from django.utils import timesince
from authentication.serializers import UserSerializer
from .models import UserComment, MatchComment, ClubComment


class UserCommentSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    time_since_created = serializers.SerializerMethodField()

    class Meta:
        model = UserComment
        fields = '__all__'

    def get_time_since_created(self, obj: UserComment):
        return timesince.timesince(obj.created_at).split(',')[0]


class MatchCommentSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    time_since_created = serializers.SerializerMethodField()
    time_since_updated = serializers.SerializerMethodField()

    class Meta:
        model = MatchComment
        fields = '__all__'

    def get_time_since_created(self, obj: MatchComment):
        return timesince.timesince(obj.created_at).split(',')[0]


class ClubCommentSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    time_since_created = serializers.SerializerMethodField()
    time_since_updated = serializers.SerializerMethodField()

    class Meta:
        model = ClubComment
        fields = '__all__'

    def get_time_since_created(self, obj: ClubComment):
        return timesince.timesince(obj.created_at).split(',')[0]
