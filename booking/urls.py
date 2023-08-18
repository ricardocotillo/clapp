from rest_framework import routers
from .views import PlaceViewSet, BookingViewSet, CourtViewSet

router = routers.SimpleRouter()
router.register('places', PlaceViewSet)
router.register('bookings', BookingViewSet)
router.register('courts', CourtViewSet)

urlpatterns = router.urls
