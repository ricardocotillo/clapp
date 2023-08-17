from rest_framework import serializers
from generic_relations.relations import GenericRelatedField
from django.contrib.contenttypes.models import ContentType
from django.utils.timesince import timesince
from authentication.serializers import UserSerializer, User, RelatedUserSerializer
from club.serializers import ClubSerializer, Club
from .models import Comment, Rating, Image


class CommentSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField()
    owner = UserSerializer(read_only=True)
    model = serializers.CharField(required=False)
    time_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'owner',
            'owner_id',
            'message',
            'model',
            'object_id',
            'created_at',
            'time_since_created',
        )
        extra_kwargs = {
            'model': {
                'write_only': True,
            },
        }

    def get_time_since_created(self, obj: Comment):
        return timesince(obj.created_at).split(',')[0]

    def create(self, validated_data: dict):
        m = validated_data.get('model')
        oi = validated_data.get('object_id')
        ct = ContentType.objects.get(model=m)
        ui = validated_data.get('owner_id')
        validated_data['content_type'] = ct
        validated_data['object_id'] = oi
        comment = Comment.objects.create(
            owner_id=ui,
            content_type=ct,
            object_id=oi,
            message=validated_data.get('message')
        )
        return comment


class RatingSerializer(serializers.ModelSerializer):
    content_object = GenericRelatedField({
        User: UserSerializer(),
        Club: ClubSerializer(),
    })
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'user', 'content_object')


class ImageSerializer(serializers.ModelSerializer):
    user = RelatedUserSerializer()

    class Meta:
        model = Image
        fields = ('id', 'image', 'description', 'user',)
