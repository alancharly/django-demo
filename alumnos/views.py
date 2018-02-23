from alumnos.models import Alumno, Nivel
from alumnos.serializers import AlumnoSerializer, NivelSerializer
from rest_framework import generics

class AlumnoList(generics.ListCreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer


class AlumnoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer


class NivelList(generics.ListCreateAPIView):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer


class NivelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer