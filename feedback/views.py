from rest_framework import viewsets
from rest_framework.response import Response
from .models import UserComment, MatchComment, ClubComment
from .serializers import UserCommentSerializer, ClubCommentSerializer, MatchCommentSerializer
from .filters import UserCommentFilter


class UserCommentViewSet(viewsets.ModelViewSet):
    queryset = UserComment.objects.order_by('-created_at')
    serializer_class = UserCommentSerializer

    def list(self, request, *args, **kwargs):
        serializer = UserCommentSerializer(
            self.filter_queryset(self.get_queryset()),
            many=True,
            context={
                'request': request,
            }
        )
        return Response(serializer.data)


class ClubCommentViewSet(viewsets.ModelViewSet):
    queryset = ClubComment.objects.order_by('-created_at')
    serializer_class = ClubCommentSerializer
    filterset_fields = ('receiver', 'sender',)


class MatchCommentViewSet(viewsets.ModelViewSet):
    queryset = MatchComment.objects.order_by('-created_at')
    serializer_class = MatchCommentSerializer
    filterset_fields = ('receiver', 'sender',)
