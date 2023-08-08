from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.page.models import Banner, Landing_Page
from apps.page.api.serializers.general_serializer import BannerSerializer, LandingSerializer


class PageViewSet(ListAPIView):
    queryset = Landing_Page.objects.all()
    serializer_class = LandingSerializer