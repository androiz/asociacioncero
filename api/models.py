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
    descripcion = models.TextField(null=False, blank=False)
    objetivo = models.FloatField(null=False, blank=False)
    recaudado = models.FloatField(null=False, blank=False, default=0)
    fecha = models.DateField(null=False, blank=False)
    prioridad = models.IntegerField(null=False, blank=False, choices=GRAVEDAD)

    imagen_principal = models.ImageField(upload_to="photo/%y%m%d", max_length=255)

    imagen1 = models.ImageField(upload_to="photo/%y%m%d", max_length=255)
    imagen2 = models.ImageField(upload_to="photo/%y%m%d", max_length=255)
    imagen3 = models.ImageField(upload_to="photo/%y%m%d", max_length=255)
    imagen4 = models.ImageField(upload_to="photo/%y%m%d", max_length=255)

    url_paypal = models.URLField(blank=True)

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

class Configuracion(models.Model):
    quienes_somos = models.TextField(null=False, blank=False)

    imagenPersona1 = models.ImageField(upload_to="config", max_length=255)
    descripcionPersona1 = models.TextField(null=False, blank=False)
    imagenPersona2 = models.ImageField(upload_to="config", max_length=255)
    descripcionPersona2 = models.TextField(null=False, blank=False)

    email = models.EmailField(null=False, blank=False)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El telefono debe tener este formato: '+999999999'. Hasta 15 digitos permitidos.")
    telefono = models.CharField(max_length=16, validators=[phone_regex], blank=False, null=False) # validators should be a list

    direccion = models.CharField(max_length=100, null=False, blank=False)

    pagina_facebook = models.URLField(blank=False)
    pagina_google = models.URLField(blank=False)
    pagina_twitter = models.URLField(blank=False)
    pagina_linkedin = models.URLField(blank=False)

    paypal_url = models.URLField(blank=False)

    def __unicode__(self):
        return "Configuracion"

    def __str__(self):
        return "Configuracion"
