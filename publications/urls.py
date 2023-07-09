from rest_framework import routers
from .views import PublicationViewSet

router = routers.SimpleRouter()
router.register('publications', PublicationViewSet)
urlpatterns = router.urls
