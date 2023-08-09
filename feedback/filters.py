from django_filters import rest_framework as filters
from .models import Comment


class CommentFilter(filters.FilterSet):
    class Meta:
        model = Comment
        fields = ('object_id', 'content_type',)
