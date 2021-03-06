# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 15:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_gatoenfermo_url_paypal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quienes_somos', models.TextField()),
                ('imagenPersona1', models.ImageField(max_length=255, upload_to='config')),
                ('descripcionPersona1', models.TextField()),
                ('imagenPersona2', models.ImageField(max_length=255, upload_to='config')),
                ('descripcionPersona2', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message="El telefono debe tener este formato: '+999999999'. Hasta 15 digitos permitidos.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
    ]
