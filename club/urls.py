from rest_framework import routers
from .views import ClubViewSet, MembershipViewSet, SportViewSet

router = routers.SimpleRouter()
router.register('clubs', ClubViewSet)
router.register('memberships', MembershipViewSet)
router.register('sports', SportViewSet)

urlpatterns = router.urls
