from rest_framework import viewsets
from django.db.models import Count
from .models import Club
from .serializers import ClubSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.annotate(
        members_count=Count('members')
    ).order_by('-created_at')
    serializer_class = ClubSerializer
