from rest_framework import routers
from .views import PlaceViewSet, BookingViewSet

router = routers.SimpleRouter()
router.register('places', PlaceViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = router.routes
