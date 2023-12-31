# Generated by Django 4.2.4 on 2023-08-04 20:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_infraestructura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landing_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('folio', models.CharField(editable=False, max_length=25, null=True, unique=True)),
                ('fecha_reg', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True, editable=False)),
                ('is_published', models.BooleanField(default=False)),
                ('is_disabled', models.BooleanField(default=False)),
                ('tema', models.CharField(blank=True, choices=[('infraestructura', 'Infraestructura'), ('inversion', 'Oportunidad de Inversión'), ('incentivos', 'Incentivos')], max_length=40, null=True, verbose_name='Elige el a cargar a informacion')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Titulo')),
                ('titulo_us', models.CharField(blank=True, max_length=100, null=True, verbose_name='Titulo en ingles')),
                ('contenido', models.CharField(blank=True, max_length=400, null=True, verbose_name='Contenido de la sección infraestructura')),
                ('contenido_us', models.CharField(blank=True, max_length=400, null=True, verbose_name='Contenido de la sección infraestructura en ingles ')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='infraestructura/', verbose_name='Imagen')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Infraestructura',
        ),
    ]
