from rest_framework import serializers
from django.utils import timesince
from authentication.serializers import UserSerializer
from .models import UserComment, MatchComment, ClubComment


class UserCommentSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.IntegerField()
    time_since_created = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserComment
        fields = (
            'id',
            'sender',
            'receiver',
            'sender_id',
            'message',
            'time_since_created',
        )

    def get_time_since_created(self, obj: UserComment):
        return timesince.timesince(obj.created_at).split(',')[0]


class MatchCommentSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.IntegerField()
    time_since_created = serializers.SerializerMethodField()

    class Meta:
        model = MatchComment
        fields = (
            'id',
            'sender',
            'receiver',
            'sender_id',
            'message',
            'time_since_created',
        )

    def get_time_since_created(self, obj: MatchComment):
        return timesince.timesince(obj.created_at).split(',')[0]


class ClubCommentSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    sender_id = serializers.IntegerField()
    time_since_created = serializers.SerializerMethodField()

    class Meta:
        model = ClubComment
        fields = (
            'id',
            'sender',
            'receiver',
            'sender_id',
            'message',
            'time_since_created',
        )

    def get_time_since_created(self, obj: ClubComment):
        return timesince.timesince(obj.created_at).split(',')[0]
