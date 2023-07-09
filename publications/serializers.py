from rest_framework import serializers
from django.utils import timesince
from authentication.serializers import UserSerializer, User
from .models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    time_since_created = serializers.SerializerMethodField()
    time_since_updated = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = '__all__'

    def get_time_since_created(self, obj: Publication):
        return timesince.timesince(obj.created_at).split(',')[0]

    def get_time_since_updated(self, obj: Publication):
        return timesince.timesince(obj.updated_at).split(',')[0]

    def create(self, validated_data: dict):
        user_data: dict = validated_data.pop('user')
        user_id = user_data.pop('id')
        user, _ = User.objects.get_or_create(id=user_id, defaults=user_data)
        validated_data['user'] = user.pk
        return super().create(validated_data)
