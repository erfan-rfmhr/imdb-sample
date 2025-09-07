from .views import RateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rate')

urlpatterns = router.urls
