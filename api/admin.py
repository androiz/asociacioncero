from django.contrib import admin
from .models import GatoEnfermo, GatoFinalFeliz, Configuracion


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
            'fields': ('imagen1', 'imagen2', 'imagen3', 'imagen4',),
        }),
    )


@admin.register(GatoFinalFeliz)
class GatoFinalFelizAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha',)
    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'imagen_principal', 'fecha',)
        }),
        ('Imagenes Extra', {
            'classes': ('collapse',),
            'fields': ('imagen1', 'imagen2', 'imagen3', 'imagen4',),
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
        ('Protocolo de Adopcion', {
            'classes': ('collapse',),
            'fields': ('protocolo_parrafo_1',)
        }),
        ('Hazte Teaming', {
            'classes': ('collapse',),
            'fields': ('teaming_parrafo_1', 'teaming_link')
        }),
        ('Ayúdanos', {
            'classes': ('collapse',),
            'fields': ('ayudanos_parrafo',)
        }),
    )
