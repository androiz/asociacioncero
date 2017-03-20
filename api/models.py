from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class GatoEnfermo(models.Model):

    BAJA = 0
    MEDIA = 1
    ALTA = 2
    URGENTE = 3

    GRAVEDAD = (
        (BAJA, 'Baja'),
        (MEDIA, 'Media'),
        (ALTA, 'Alta'),
        (URGENTE, 'Urgente')
    )

    nombre = models.CharField(max_length=255, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=True)
    objetivo = models.FloatField(null=False, blank=True)
    recaudado = models.FloatField(null=False, blank=True, default=0)
    fecha = models.DateField(null=False, blank=True)
    prioridad = models.IntegerField(null=False, blank=True, choices=GRAVEDAD)

    imagen_principal = models.ImageField(upload_to="photo/%y%m%d", max_length=255)

    imagen1 = models.ImageField(upload_to="photo/%y%m%d", max_length=255, null=True, blank=True)
    imagen2 = models.ImageField(upload_to="photo/%y%m%d", max_length=255, null=True, blank=True)
    imagen3 = models.ImageField(upload_to="photo/%y%m%d", max_length=255, null=True, blank=True)
    imagen4 = models.ImageField(upload_to="photo/%y%m%d", max_length=255, null=True, blank=True)

    url_paypal = models.URLField(blank=True)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

class Configuracion(models.Model):
    quienes_somos = models.TextField(null=False, blank=False)

    imagen_principal = models.ImageField(upload_to="config", max_length=255, null=False, blank=False)

    imagenPersona1 = models.ImageField(upload_to="config", max_length=255, null=True, blank=True)
    descripcionPersona1 = models.TextField(null=False, blank=True)
    imagenPersona2 = models.ImageField(upload_to="config", max_length=255, null=True, blank=True)
    descripcionPersona2 = models.TextField(null=False, blank=True)

    email = models.EmailField(null=False, blank=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El telefono debe tener este formato: '+999999999'. Hasta 15 digitos permitidos.")
    telefono = models.CharField(max_length=16, validators=[phone_regex], blank=True, null=True) # validators should be a list

    direccion = models.CharField(max_length=100, null=True, blank=True)

    pagina_facebook = models.URLField(blank=True)
    pagina_google = models.URLField(blank=True)
    pagina_twitter = models.URLField(blank=True)
    pagina_linkedin = models.URLField(blank=True)

    paypal_url = models.URLField(blank=True)

    def __unicode__(self):
        return "Configuracion"

    def __str__(self):
        return "Configuracion"
