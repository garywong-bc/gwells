# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0009_auto_20171109_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yieldestimationmethod',
            old_name='yield_estimated_method_code',
            new_name='yield_estimation_method_code',
        ),
    ]