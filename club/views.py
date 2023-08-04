from rest_framework import viewsets
from .models import Club


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.order_by('id')
