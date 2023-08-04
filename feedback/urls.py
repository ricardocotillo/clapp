from rest_framework import routers
from .views import UserCommentViewSet, ClubCommentViewSet, MatchCommentViewSet

router = routers.SimpleRouter()
router.register('user-comments', UserCommentViewSet)
router.register('club-comments', ClubCommentViewSet)
router.register('match-comments', MatchCommentViewSet)

urlpatterns = router.urls
