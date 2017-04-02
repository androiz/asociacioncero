from rest_framework import serializers
from .models import GatoEnfermo, GatoFinalFeliz, Configuracion


# Serializers define the API representation.
class GatoEnfermoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GatoEnfermo
        fields = '__all__'


class GatoFinalFelizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GatoFinalFeliz
        fields = '__all__'


class ConfiguracionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Configuracion
        fields = '__all__'
