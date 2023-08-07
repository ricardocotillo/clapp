from rest_framework import viewsets, filters
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-id')
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'first_name', 'last_name',)
