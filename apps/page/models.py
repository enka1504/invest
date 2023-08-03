from django.db import models
from apps.base.models import BaseModel

class Banner(BaseModel):
    identifier = 'BN'
    titulo = models.CharField('Titulo',max_length=100, blank=True, null=True)
    titulo_us = models.CharField('Titulo en ingles',max_length=100, blank=True, null=True)
    contenido = models.CharField('Contenido del banner', max_length=400, blank=True, null=True)
    contenido_us = models.CharField('Contenido en ingles del banner', max_length=400, blank=True, null=True)
    comentario = models.CharField('Comentarios', max_length=200, blank=True, null=True)
    comentario_us = models.CharField('Comentarios en ingles', max_length=200, blank=True, null=True)
    multimedia = models.FileField('Video banner', upload_to = 'banner/', blank=True, null=True)
    imagen = models.ImageField('Imagen',upload_to = 'banner/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Infraestructura(BaseModel):
    titulo = models.CharField('Titulo',max_length=100, blank=True, null=True)
    titulo_us = models.CharField('Titulo en ingles',max_length=100, blank=True, null=True)
    contenido = models.CharField('Contenido del banner', max_length=400, blank=True, null=True)
    contenido_us = models.CharField('Contenido en ingles del banner', max_length=400, blank=True, null=True)
    imagen = models.ImageField('Imagen',upload_to = 'infraestructura/', blank=True, null=True)