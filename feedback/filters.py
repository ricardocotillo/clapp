import django_filters
from .models import UserComment


class UserCommentFilter(django_filters.FilterSet):
    receiver_me = django_filters.BooleanFilter(method='filter_receiver_me')
    sender_me = django_filters.BooleanFilter(method='filter_sender_me')

    class Meta:
        model = UserComment
        fields = ('sender_me', 'receiver_me',)

    def filter_receiver_me(self, queryset, name, value):
        print(name)
        print(value)
        return queryset.filter(receiver=self.request.user)

    def filter_receiver_me(self, queryset, name, value):
        return queryset.filter(sender=self.request.user)
