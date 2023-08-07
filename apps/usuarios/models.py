# Django
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class Usuarios(AbstractUser):
    class Meta:
        ordering = ['-is_superuser', 'date_joined']
        default_permissions = []
        permissions = [
            ('view_users', 'Ver usuarios'),
            ('create_users', 'Crear usuarios'),
            ('list_users', 'Listar usuarios'),
            ('edit_users', 'Editar usuarios')
        ]
    first_name = None
    last_name = None
    username = models.CharField('Nombre de usuario', max_length = 100, null = True, blank = True, unique=True)
    full_name = models.CharField('Nombre completo', max_length = 150) 
    email = models.EmailField('Correo electrónico', unique=True)
    phone_number = models.CharField('Número de teléfono', max_length=10, unique = True)
    sex = models.CharField('Sexo', max_length = 10, choices = [('h', 'Masculino'), ('m', 'Femenino')])
    work_shift = models.CharField('Turno', max_length = 10, choices = [('matutino', 'Matutino'), ('vespertino', 'Vespertino'), ('nocturno', 'Nocturno')])
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'full_name', 'username']