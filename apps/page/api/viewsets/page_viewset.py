import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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

class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        # Enviar el correo electrónico
        try:
            email = request.data['email']
            name = request.data['name']
            subject = 'Nuevo mensaje de contacto'
            message = f'Nombre: {name}\nCorreo: {email}\n\n{request.data["message"]}'
            
            msg = MIMEMultipart()
            msg['From'] = request.data['email']
            msg['To'] = settings.EMAIL_HOST_USER  # Tu correo institucional
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            
            server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(settings.EMAIL_HOST_USER, msg['To'], msg.as_string())
            server.quit()
        
        except Exception as e:
            error_message = 'Ocurrió un problema al enviar el mensaje. Por favor, inténtelo de nuevo más tarde.'
            print(f'Error al enviar correo electrónico: {e}')
            # Enviar un correo electrónico de error
            #send_error_email(f'Error al enviar correo electrónico: {str(e)}')
            
            # Devolver una respuesta de error al cliente
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        