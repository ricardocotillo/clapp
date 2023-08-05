from django_filters import rest_framework as filters
from .models import UserComment, ClubComment


class UserCommentFilter(filters.FilterSet):
    receiver_me = filters.BooleanFilter(
        field_name='receiver',
        method='filter_receiver_me',
    )
    sender_me = filters.BooleanFilter(
        field_name='sender',
        method='filter_sender_me',
    )

    class Meta:
        model = UserComment
        fields = ('receiver', 'sender',)

    def filter_receiver_me(self, queryset, name, value):
        return queryset.filter(receiver=self.request.user)

    def filter_sender_me(self, queryset, name, value):
        return queryset.filter(sender=self.request.user)


class ClubCommentFilter(filters.FilterSet):
    class Meta:
        model = ClubComment
        fields = ('receiver', 'sender')
