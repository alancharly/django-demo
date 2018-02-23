from rest_framework import serializers
from alumnos.models import Nivel, Alumno


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id', 'nombre', 'genero', 'nivel')


class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = ('id', 'descripcion')
