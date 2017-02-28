from rest_framework import viewsets
from .models import GatoEnfermo, Configuracion
from .serializers import GatoEnfermoSerializer, ConfiguracionSerializer

# ViewSets define the view behavior.
class GatoEnfermoViewSet(viewsets.ModelViewSet):
    queryset = GatoEnfermo.objects.all()
    serializer_class = GatoEnfermoSerializer

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer