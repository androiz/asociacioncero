from django.contrib import admin
from .models import GatoEnfermo, Configuracion

# Register your models here.
@admin.register(GatoEnfermo)
class GatoEnfermmoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'objetivo', 'prioridad')
    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'imagen_principal',
                       'prioridad', 'en_adopcion', )
        }),
        ('Recaudar', {
            'classes': ('collapse',),
            'fields': ('recaudar', 'objetivo', 'recaudado', 'fecha',
                       'url_paypal'),
        }),
        ('Imagenes Extra', {
            'classes': ('collapse',),
            'fields': ('imagen1', 'imagen2', 'imagen3',),
        }),
    )

@admin.register(Configuracion)
class ConfiguracionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'imagen_principal', 'pagina_facebook',
                       'pagina_instagram', 'paypal_url', )
        }),
        ('Quienes Somos', {
            'classes': ('collapse',),
            'fields': ('quienes_somos',),
        }),
    )