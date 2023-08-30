from rest_framework import viewsets
from django.db.models import Count
from django.db.models.functions import Coalesce
from utils.models import Sport
from .models import Club, Membership, Scrimmage, ScrimmageUser
from .serializers import ClubSerializer, MembershipSerializer, SportSerializer, ScrimmageSerializer, ScrimmageUserSerializer
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


class ScrimmageViewSet(viewsets.ModelViewSet):
    queryset = Scrimmage.objects.order_by('-created_at')
    serializer_class = ScrimmageSerializer


class ScrimmageUserViewSet(viewsets.ModelViewSet):
    queryset = ScrimmageUser.objects.order_by('-created_at')
    serializer_class = ScrimmageUserSerializer
