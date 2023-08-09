from rest_framework import serializers
from generic_relations.relations import GenericRelatedField
from django.contrib.contenttypes.models import ContentType
from authentication.serializers import UserSerializer, User
from club.serializers import ClubSerializer, Club
from .models import Comment, Rating


class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    user = UserSerializer(read_only=True)
    model = serializers.CharField(required=False)

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'user_id',
            'message',
            'model',
            'object_id',
            'created_at',
        )
        extra_kwargs = {
            'model': {
                'write_only': True,
            }
        }

    def create(self, validated_data: dict):
        m = validated_data.get('model')
        oi = validated_data.get('object_id')
        ct = ContentType.objects.get(model=m)
        ui = validated_data.get('user_id')
        validated_data['content_type'] = ct
        validated_data['object_id'] = oi
        comment = Comment.objects.create(
            user_id=ui,
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
