from rest_framework import viewsets
from django.db.models import Count
from .models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.annotate(
        reactions_count=Count('reactions')
    ).order_by('-updated_at')
    serializer_class = PublicationSerializer
