from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import generics, status

from apps.page.models import Banner, Landing_Page, ContactMessage
from apps.page.api.serializers.general_serializer import LandingSerializer, ContactSerializer


class PageViewSet(ListAPIView):
    queryset = Landing_Page.objects.all()
    serializer_class = LandingSerializer

class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            subject = request.data.get('subject', '')
            message = request.data.get('message', '')
            from_email = request.data.get('email', '')

            # Enviar correo
            send_mail(
                subject,
                message,
                from_email,
                ['invest.sedec@tabasco.gob.mx'],
                fail_silently=False,
            )

            # Guardar mensaje en el modelo
            contact_message = ContactMessage(
                name=request.data.get('name', ''),
                email=from_email,
                subject=subject,
                message=message
            )
            contact_message.save()

            return Response({'message': 'Correo enviado correctamente'}, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({'error': 'Error al enviar el correo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)