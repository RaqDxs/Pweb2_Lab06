from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/crear/', views.crear_alumno, name='crear_alumno'),
]