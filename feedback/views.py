from rest_framework import viewsets
from .models import UserComment, MatchComment, ClubComment
from .serializers import UserCommentSerializer, ClubCommentSerializer, MatchCommentSerializer
from .filters import UserCommentFilter, ClubCommentFilter


class UserCommentViewSet(viewsets.ModelViewSet):
    queryset = UserComment.objects.order_by('-created_at')
    serializer_class = UserCommentSerializer
    filterset_class = UserCommentFilter


class ClubCommentViewSet(viewsets.ModelViewSet):
    queryset = ClubComment.objects.order_by('-created_at')
    serializer_class = ClubCommentSerializer
    filterset_class = ClubCommentFilter


class MatchCommentViewSet(viewsets.ModelViewSet):
    queryset = MatchComment.objects.order_by('-created_at')
    serializer_class = MatchCommentSerializer
    filterset_fields = ('receiver', 'sender',)
