from rest_framework import viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from .models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.order_by('-updated_at')
    serializer_class = PublicationSerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]