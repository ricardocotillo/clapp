from django_filters import rest_framework as filters
from utils.filters import NumberInFilter
from .models import Membership, Club


class MembershipFilter(filters.FilterSet):
    class Meta:
        model = Membership
        fields = ('club',)


class ClubFilter(filters.FilterSet):
    sport = NumberInFilter()

    class Meta:
        model = Club
        fields = ('owner', 'members', 'sport')
