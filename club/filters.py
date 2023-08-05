from django_filters import rest_framework as filters
from .models import Membership


class MembershipFilter(filters.FilterSet):
    class Meta:
        model = Membership
        fields = ('club',)
