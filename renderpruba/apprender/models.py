from django.db import models

# Create your models here.

class usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    clave = models.CharField(max_length=10)
    correo = models.CharField(max_length=30);
    foto_perfil = models.ImageField(upload_to='usuarios/', default='usuarios/imagen.png')

    class Meta:
        managed = True
