from django.urls import path
from .views import crear_alumno, crear_curso, ingresar_nota, lista_alumnos, lista_cursos, lista_notas

urlpatterns = [
    path('crear_alumno/', crear_alumno, name='crear_alumno'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('ingresar_nota/', ingresar_nota, name='ingresar_nota'),
    path('lista_alumnos/', lista_alumnos, name='lista_alumnos' ),
    path('lista_cursos/', lista_cursos, name='lista_cursos' ),
    path('lista_notas/', lista_notas, name='lista_notas' ),
]
