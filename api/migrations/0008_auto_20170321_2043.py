# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170320_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuracion',
            old_name='pagina_google',
            new_name='pagina_instagram',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='descripcionPersona1',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='descripcionPersona2',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='imagenPersona1',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='imagenPersona2',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='pagina_linkedin',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='pagina_twitter',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='telefono',
        ),
    ]
