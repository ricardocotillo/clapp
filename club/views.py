from rest_framework import viewsets
from django.db.models import Count
from .models import Club, Membership
from .serializers import ClubSerializer, MembershipSerializer
from .filters import MembershipFilter, ClubFilter


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.annotate(
        members_count=Count('members')
    ).order_by('-created_at')
    serializer_class = ClubSerializer
    filterset_class = ClubFilter


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    filterset_class = MembershipFilter
