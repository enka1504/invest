from django.db import models
from apps.base.models import BaseModel
from apps.base.validators import validate_pdf_file


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

class Landing_Page(BaseModel):
    tema_choices = (
        ('infraestructura','Infraestructura y logistica'),
        ('inversion', 'Oportunidad de Inversión'),
        ('incentivos', 'Incentivos'),
        ('real-state','Real State'),
        ('dossier', 'Dossier de inversión')
    )
    tema = models.CharField('Elige tema a cargar a informacion', choices=tema_choices, max_length=40, blank=True, null=True)
    titulo = models.CharField('Titulo',max_length=100, blank=True, null=True)
    titulo_us = models.CharField('Titulo en ingles',max_length=100, blank=True, null=True)
    contenido = models.CharField('Contenido de la sección infraestructura', max_length=400, blank=True, null=True)
    contenido_us = models.CharField('Contenido de la sección infraestructura en ingles ', max_length=400, blank=True, null=True)
    imagen = models.ImageField('Imagen',upload_to = 'landing-page/', blank=True, null=True)
    pdf = models.FileField('Selecionar pdf para descargar',upload_to='landing-page', validators=[validate_pdf_file], null=True, blank=True)
    

    def __str__(self):
        return self.titulo

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)