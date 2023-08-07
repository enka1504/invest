from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.page.models import Banner, Landing_Page
from apps.page.api.serializers.general_serializer import BannerSerializer, LandingSerializer


class IndexViewSet(APIView):

    def get(self, request):
        banners = Banner.objects.all()
        landing_pages = Landing_Page.objects.all()

        banner_serializer = BannerSerializer(banners, many=True)
        landing_page_serializer = LandingSerializer(landing_pages, many=True)

        data = {
            'banners': banner_serializer.data,
            'landing_pages': landing_page_serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework import status

# from apps.page.models import Banner, Landing_Page
# from apps.page.api.serializers.general_serializer import BannerSerializer, LandingSerializer

# class IndexViewSet(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'page/index.html'

#     def get(self, request):
#         banners = Banner.objects.all()
#         landing_pages = Landing_Page.objects.all()

#         banner_serializer = BannerSerializer(banners, many=True)
#         landing_page_serializer = LandingSerializer(landing_pages, many=True)

#         data = {
#             'banners': banner_serializer.data,
#             'landing_pages': landing_page_serializer.data
#         }

#         return Response({'data': data}, status=status.HTTP_200_OK)
# from django.views.generic import TemplateView
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.renderers import TemplateHTMLRenderer

# from apps.page.models import Banner, Landing_Page
# from apps.page.api.serializers.general_serializer import BannerSerializer, LandingSerializer


# class IndexView(TemplateView):
#     template_name = 'page/index.html'

#     def get_context_data(self, **kwargs):
#         banners = Banner.objects.all()
#         landing_pages = Landing_Page.objects.all()

#         banner_serializer = BannerSerializer(banners, many=True)
#         landing_page_serializer = LandingSerializer(landing_pages, many=True)

#         data = {
#             'banners': banner_serializer.data,
#             'landing_pages': landing_page_serializer.data
#         }
#         print(data)
#         return {'data': data}

#     def render_to_response(self, context, **response_kwargs):
#         return self.response_class(
#             request=self.request,
#             template=self.get_template_names(),
#             context=context,
#             **response_kwargs
#         )
