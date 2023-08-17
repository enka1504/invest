from rest_framework import routers
from django.urls import path
from apps.page.api.viewsets.general_viewset import BannerViewSet
from apps.page.api.viewsets.page_viewset import PageViewSet, ContactCreateView

router = routers.DefaultRouter()
router.register(r'banners', BannerViewSet)

#urlpatterns = router.urls
urlpatterns = [
    path('banners/', BannerViewSet.as_view(), name='banner-list'),
    path('page/', PageViewSet.as_view(), name='page-list'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
]
