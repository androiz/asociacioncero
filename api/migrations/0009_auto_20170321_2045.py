# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170321_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='imagen_principal',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='config'),
        ),
    ]
