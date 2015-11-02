# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0002_auto_20151025_1950'),
        ('dataexchanges', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='third_party_name_2',
        ),
        migrations.RemoveField(
            model_name='report',
            name='third_party_name_3',
        ),
        migrations.RemoveField(
            model_name='report',
            name='third_party_name',
        ),
        migrations.AddField(
            model_name='report',
            name='third_party_name',
            field=models.ManyToManyField(to='stakeholders.Stakeholder', null=True),
        ),
    ]
