from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from apps.page.models import Banner, Landing_Page
from apps.page.api.serializers.general_serializer import BannerSerializer, LandingSerializer

class BannerViewSet(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
