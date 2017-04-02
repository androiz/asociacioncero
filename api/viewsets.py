from rest_framework import viewsets
from .models import GatoEnfermo, GatoFinalFeliz, Configuracion
from .serializers import GatoEnfermoSerializer, GatoFinalFelizSerializer, ConfiguracionSerializer


# ViewSets define the view behavior.
class GatoEnfermoViewSet(viewsets.ModelViewSet):
    queryset = GatoEnfermo.objects.all()
    serializer_class = GatoEnfermoSerializer


class GatoFinalFelizViewSet(viewsets.ModelViewSet):
    queryset = GatoFinalFeliz.objects.all()
    serializer_class = GatoFinalFelizSerializer


class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer
