from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from alumnos import views

urlpatterns = [
    url(r'^alumno/$', views.AlumnoList.as_view()),
    url(r'^alumno/(?P[0-9]+)/$', views.AlumnoDetail.as_view()),
    url(r'^nivel/$', views.NivelList.as_view()),
    url(r'^nivel/(?P[0-9]+)/$', views.NivelDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)