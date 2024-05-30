from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('academia/', include('academia.urls')),
]

# Configuración de archivos estáticos en modo de desarrollo
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)