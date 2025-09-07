from rest_framework.routers import DefaultRouter

from .views import RateViewSet

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rate')

urlpatterns = router.urls
