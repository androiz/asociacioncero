from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class GatoEnfermo(models.Model):

    BAJA = 1
    MEDIA = 2
    ALTA = 3
    URGENTE = 4

    GRAVEDAD = (
        (BAJA, 'Baja'),
        (MEDIA, 'Media'),
        (ALTA, 'Alta'),
        (URGENTE, 'Urgente')
    )

    nombre = models.CharField(max_length=255, null=False, blank=False)
    descripcion = RichTextField(null=False, blank=False)
    imagen_principal = models.ImageField(upload_to="photo/%y%m%d", max_length=255)
    prioridad = models.IntegerField(null=True, blank=True, choices=GRAVEDAD)

    en_adopcion = models.BooleanField(default=False)

    # Recaudatorio
    recaudar = models.BooleanField(default=False)
    objetivo = models.FloatField(null=True, blank=True)
    recaudado = models.FloatField(null=True, blank=True, default=0)
    fecha = models.DateField(null=True, blank=True)
    url_paypal = models.URLField(blank=True)

    # Extra imagenes
    imagen1 = models.ImageField(upload_to="photo/%y%m%d", max_length=255, null=True, blank=True)
    imagen2 = models.ImageField(upload_to="photo/%y%m%d", max_length=255, null=True, blank=True)
    imagen3 = models.ImageField(upload_to="photo/%y%m%d", max_length=255, null=True, blank=True)
    imagen4 = models.ImageField(upload_to="photo/%y%m%d", max_length=255, null=True, blank=True)

    # Protocolo Adoption

    # Hazte Teaming

    class Meta:
        verbose_name_plural = "Gatos Enfermos"

    def __unicode__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

class Configuracion(models.Model):

    imagen_principal = models.ImageField(upload_to="config", max_length=255, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    pagina_facebook = models.URLField(blank=True)
    pagina_instagram = models.URLField(blank=True)
    paypal_url = models.URLField(blank=True)

    # Seccion Quienes Somos
    quienes_somos = RichTextField()

    class Meta:
        verbose_name_plural = "Configuracion"

    def __unicode__(self):
        return "Configuracion"

    def __str__(self):
        return "Configuracion"
