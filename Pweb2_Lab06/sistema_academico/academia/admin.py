from django.contrib import admin
from .models import Alumno, Curso, NotasAlumnosPorCurso

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'matricula')
    search_fields = ('nombre', 'apellido', 'email', 'matricula')

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Curso)
admin.site.register(NotasAlumnosPorCurso)

# Register your models here.
