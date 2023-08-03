from rest_framework import routers
from apps.page.api.viewsets.general_viewset import BannerViewSet

router = routers.DefaultRouter()
router.register(r'banners', BannerViewSet)

urlpatterns = router.urls