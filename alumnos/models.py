from django.db import models

# Create your models here.
class Nivel(models.Model):
    descripcion = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('descripcion',)

class Alumno(models.Model):
    nombre = models.CharField(max_length=100, blank=True, default='')
    genero = models.CharField(max_length=100, blank=True, default='')
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    class Meta:
        ordering = ('nombre',)