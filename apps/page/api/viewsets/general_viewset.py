from rest_framework import viewsets
from apps.page.models import Banner
from apps.page.api.serializers.general_serializer import BannerSerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from .models import Banner
# from .serializers import BannerSerializer
# from .utils import validate_files

# class BannerViewSet(viewsets.ModelViewSet):
#     queryset = Banner.objects.filter(state=True)
#     serializer_class = BannerSerializer
#     parser_classes = (JSONParser, MultiPartParser, )

#     @action(detail=True, methods=['get'])
#     def retrieve(self, request, pk=None):
#         banner = get_object_or_404(self.queryset, id=pk)
#         banner_serializer = BannerSerializer(banner)
#         return Response(banner_serializer.data, status=status.HTTP_200_OK)

#     @action(detail=True, methods=['put'])
#     def update(self, request, pk=None):
#         banner = get_object_or_404(self.queryset, id=pk)
#         data = validate_files(request.data, 'imagen', True)
#         banner_serializer = self.serializer_class(banner, data=data)
#         if banner_serializer.is_valid():
#             banner_serializer.save()
#             return Response({'message': 'Banner actualizado correctamente!'}, status=status.HTTP_200_OK)
#         return Response({'message': '', 'error': banner_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     @action(detail=True, methods=['delete'])
#     def destroy(self, request, pk=None):
#         banner = get_object_or_404(self.queryset, id=pk)
#         banner.state = False
#         banner.save()
#         return Response({'message': 'Banner eliminado correctamente!'}, status=status.HTTP_200_OK)

#     def list(self, request):
#         banners = self.queryset
#         banner_serializer = self.get_serializer(banners, many=True)
#         data = {
#             "total": banners.count(),
#             "totalNotFiltered": banners.count(),
#             "rows": banner_serializer.data
#         }
#         return Response(data, status=status.HTTP_200_OK)

#     def create(self, request):
#         data = validate_files(request.data, 'imagen')
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Banner creado correctamente!'}, status=status.HTTP_201_CREATED)
#         return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)