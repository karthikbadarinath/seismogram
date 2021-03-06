# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seismic_events', '0002_auto_20170528_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seismicevent',
            name='depth',
            field=models.DecimalField(decimal_places='5', max_digits='10'),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='fac',
            field=models.DecimalField(decimal_places='5', max_digits='10', null=True),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='lat',
            field=models.DecimalField(decimal_places='5', max_digits='10'),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='lon',
            field=models.DecimalField(decimal_places='5', max_digits='10'),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='mo',
            field=models.DecimalField(decimal_places='5', max_digits='10', null=True),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='mpp',
            field=models.DecimalField(decimal_places='5', max_digits='10', null=True),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='mpr',
            field=models.DecimalField(decimal_places='5', max_digits='10', null=True),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='mrr',
            field=models.DecimalField(decimal_places='5', max_digits='10', null=True),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='mrt',
            field=models.DecimalField(decimal_places='5', max_digits='10', null=True),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='mtp',
            field=models.DecimalField(decimal_places='5', max_digits='10', null=True),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='mtt',
            field=models.DecimalField(decimal_places='5', max_digits='10', null=True),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='mw',
            field=models.DecimalField(decimal_places='5', max_digits='10'),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='smajax',
            field=models.DecimalField(decimal_places='5', max_digits='10'),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='sminax',
            field=models.DecimalField(decimal_places='5', max_digits='10'),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='strike',
            field=models.DecimalField(decimal_places='5', max_digits='10'),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='unc',
            field=models.DecimalField(decimal_places='5', max_digits='10'),
        ),
        migrations.AlterField(
            model_name='seismicevent',
            name='unc_1',
            field=models.DecimalField(decimal_places='5', max_digits='10'),
        ),
    ]
