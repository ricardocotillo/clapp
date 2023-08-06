from django_filters import rest_framework as filters
from .models import Membership, Club


class MembershipFilter(filters.FilterSet):
    class Meta:
        model = Membership
        fields = ('club',)


class ClubFilter(filters.FilterSet):
    sport = filters.NumberFilter(
        field_name='sport',
        method='filter_sport',
    )

    class Meta:
        model = Club
        fields = ('owner', 'members', 'sport')

    def filter_sport(self, queryset, name, value):
        sports = self.request.GET.getlist('sport')
        sports = [int(s) for s in sports]
        return queryset.filter(sport__in=sports)
