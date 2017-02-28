from django.contrib import admin
from .models import GatoEnfermo, Configuracion

# Register your models here.
@admin.register(GatoEnfermo)
class GatoEnfermmoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'objetivo', 'prioridad')

@admin.register(Configuracion)
class ConfiguracionAdmin(admin.ModelAdmin):
    pass