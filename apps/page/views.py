from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import status

from .models import Banner, Landing_Page
from apps.page.api.serializers.general_serializer import BannerSerializer, LandingSerializer


class Index(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        banners = Banner.objects.all()
        landing_pages = Landing_Page.objects.all()

        banner_serializer = BannerSerializer(banners, many=True)
        landing_page_serializer = LandingSerializer(landing_pages, many=True)

        context['banners'] = banner_serializer.data
        context['landing_pages'] = landing_page_serializer.data
        
        return context

# from django.views.generic.base import RedirectView, TemplateView

# class Index(TemplateView):
#     template_name = 'pages/index.html'