"""asociacioncero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

from api.viewsets import GatoEnfermoViewSet, GatoFinalFelizViewSet, ConfiguracionViewSet

router = routers.DefaultRouter()
router.register(r'gato_enfermo', GatoEnfermoViewSet)
router.register(r'gato_final_feliz', GatoFinalFelizViewSet)
router.register(r'configuracion', ConfiguracionViewSet)

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^auth_api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)