from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/crear/', views.crear_alumno, name='crear_alumno'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('notas/ingresar/', views.ingresar_nota, name='ingresar_nota'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('notas/', views.lista_notas, name='lista_notas'),
]
