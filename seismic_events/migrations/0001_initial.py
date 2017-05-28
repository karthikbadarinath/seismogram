# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeismicEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventid', models.IntegerField()),
                ('event_date', models.DateTimeField()),
                ('lat', models.DecimalField(decimal_places='20', max_digits='20')),
                ('lon', models.DecimalField(decimal_places='20', max_digits='20')),
                ('smajax', models.DecimalField(decimal_places='20', max_digits='20')),
                ('sminax', models.DecimalField(decimal_places='20', max_digits='20')),
                ('strike', models.DecimalField(decimal_places='20', max_digits='20')),
                ('q', models.CharField(max_length=10)),
                ('depth', models.DecimalField(decimal_places='20', max_digits='20')),
                ('unc', models.DecimalField(decimal_places='20', max_digits='20')),
                ('q_1', models.CharField(max_length=10)),
                ('mw', models.DecimalField(decimal_places='20', max_digits='20')),
                ('unc_1', models.DecimalField(decimal_places='20', max_digits='20')),
                ('q_2', models.CharField(max_length=10)),
                ('s', models.CharField(max_length=10)),
                ('mo', models.DecimalField(decimal_places='20', max_digits='20')),
                ('fac', models.DecimalField(decimal_places='20', max_digits='20')),
                ('mo_auth', models.CharField(max_length=10)),
                ('mpp', models.DecimalField(decimal_places='20', max_digits='20')),
                ('mpr', models.DecimalField(decimal_places='20', max_digits='20')),
                ('mrr', models.DecimalField(decimal_places='20', max_digits='20')),
                ('mrt', models.DecimalField(decimal_places='20', max_digits='20')),
                ('mtp', models.DecimalField(decimal_places='20', max_digits='20')),
                ('mtt', models.DecimalField(decimal_places='20', max_digits='20')),
            ],
        ),
    ]
