from rest_framework import viewsets
from .models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.order_by('-updated_at')
    serializer_class = PublicationSerializer

    def create(self, request, *args, **kwargs):
        print(request.POST)
        return
        return super().create(request, *args, **kwargs)
