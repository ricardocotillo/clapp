from rest_framework import serializers
from generic_relations.relations import GenericRelatedField
from django.utils import timesince
from authentication.serializers import UserSerializer, User
from club.serializers import ClubSerializer, Club
from .models import Comment, Rating


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'message', 'created_at',)


class RatingSerializer(serializers.ModelSerializer):
    content_object = GenericRelatedField({
        User: UserSerializer(),
        Club: ClubSerializer(),
    })
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'user', 'content_object')
