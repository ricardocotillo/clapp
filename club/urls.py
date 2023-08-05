from rest_framework import routers
from .views import ClubViewSet, MembershipViewSet

router = routers.SimpleRouter()
router.register('clubs', ClubViewSet)
router.register('memberships', MembershipViewSet)

urlpatterns = router.urls
