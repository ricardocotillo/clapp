from rest_framework import serializers
from django.utils import timesince
from authentication.serializers import UserSerializer
from .models import Publication
from .fields import Base64ImageField


class PublicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    image = Base64ImageField(required=False, allow_null=True)
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
        user = self.context.get('request').user
        return Publication.objects.create(user=user, **validated_data)
