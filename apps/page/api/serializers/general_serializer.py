from apps.page.models import Banner, Landing_Page, ContactMessage

from rest_framework import serializers

# class BannerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Banner

#     def to_representation(self, instance):
#         return{
#             'id': instance.id,
#             'titulo': instance.titulo,
#             'titulo_us': instance.titulo_us,
#             'contenido': instance.contenido,
#             'contenido_us': instance.contenido_us,
#             'comentario': instance.comentario,
#             'comentario_us': instance.comentario_us,
#             'multimedia': instance.multimedia,
#             'imagen': instance.imagen
#         }
class BannerSerializer(serializers.ModelSerializer):
    multimedia = serializers.SerializerMethodField()
    imagen = serializers.SerializerMethodField()

    def get_multimedia(self, obj):
        return str(obj.multimedia)

    def get_imagen(self, obj):
        return str(obj.imagen)

    class Meta:
        model = Banner
        fields = '__all__'

class LandingSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()
    def get_imagen(self, obj):
        return str(obj.imagen)

    class Meta:
        model = Landing_Page
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        
