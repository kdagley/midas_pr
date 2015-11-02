# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataexchanges', '0002_auto_20151025_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='third_party_name',
            field=models.ManyToManyField(to='stakeholders.Stakeholder'),
        ),
    ]
