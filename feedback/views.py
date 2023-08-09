from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from .filters import CommentFilter


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.order_by('-created_at')
    serializer_class = CommentSerializer
    filterset_class = CommentFilter
