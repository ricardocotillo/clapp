from rest_framework import routers
from .views import ClubViewSet

router = routers.SimpleRouter()
router.register('clubs', ClubViewSet)

urlpatterns = router.urls
