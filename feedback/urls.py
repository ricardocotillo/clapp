from rest_framework import routers
from .views import CommentViewSet

router = routers.SimpleRouter()
router.register('comments', CommentViewSet)

urlpatterns = router.urls
