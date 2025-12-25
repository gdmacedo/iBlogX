"""
Projeto.......: iBlogX - Blog para um clínica veterinária.
File..........: urls.py : URL configuration for _iBlogXApp project.
Author........: Macedo, Glener Diniz - Engenheiro de Software - Developer Full Stack
Data Inicial..: 2025, Dezembro, 22 - Última Alteração: 2025-12-23


"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('iClynikaX.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
