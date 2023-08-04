from rest_framework import viewsets
from .models import UserComment, MatchComment, ClubComment
from .serializers import UserCommentSerializer, ClubCommentSerializer, MatchCommentSerializer


class UserCommentViewSet(viewsets.ModelViewSet):
    queryset = UserComment.objects.order_by('id')
    serializer_class = UserCommentSerializer


class ClubCommentViewSet(viewsets.ModelViewSet):
    queryset = ClubComment.objects.all()
    serializer_class = ClubCommentSerializer


class MatchCommentViewSet(viewsets.ModelViewSet):
    queryset = MatchComment.objects.all()
    serializer_class = MatchCommentSerializer
