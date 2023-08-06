from django_filters import rest_framework as filters
from .models import Membership, Club


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class MembershipFilter(filters.FilterSet):
    class Meta:
        model = Membership
        fields = ('club',)


class ClubFilter(filters.FilterSet):
    sport = NumberInFilter()

    class Meta:
        model = Club
        fields = ('owner', 'members', 'sport')
