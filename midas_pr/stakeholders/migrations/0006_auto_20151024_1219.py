# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0005_auto_20151024_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory_name',
            field=models.CharField(default=b'None', max_length=200),
        ),
    ]
