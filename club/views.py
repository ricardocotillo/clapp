from rest_framework import viewsets
from django.db.models import Count
from django.db.models.functions import Coalesce
from .models import Club, Membership, Sport
from .serializers import ClubSerializer, MembershipSerializer, SportSerializer
from .filters import MembershipFilter, ClubFilter


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.annotate(
        members_count=Coalesce(Count('members'), 0)
    ).order_by('-created_at')
    serializer_class = ClubSerializer
    filterset_class = ClubFilter


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.order_by('-role', '-created_at')
    serializer_class = MembershipSerializer
    filterset_class = MembershipFilter


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.order_by('name')
    serializer_class = SportSerializer
