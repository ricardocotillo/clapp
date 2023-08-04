from rest_framework import serializers
from .models import UserComment, MatchComment, ClubComment


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = '__all__'


class MatchCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchComment
        fields = '__all__'


class ClubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubComment
        fields = '__all__'
