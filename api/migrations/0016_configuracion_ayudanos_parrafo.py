# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 19:22
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_configuracion_teaming_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='ayudanos_parrafo',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
