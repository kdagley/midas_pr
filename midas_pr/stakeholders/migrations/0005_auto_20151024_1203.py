# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0004_auto_20151023_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcategory_name', models.CharField(default=b'Unknown', unique=True, max_length=200)),
                ('category', models.ForeignKey(default=1, to='stakeholders.Category', null=True)),
            ],
            options={
                'verbose_name_plural': 'subcategories',
            },
        ),
        migrations.RemoveField(
            model_name='stakeholder',
            name='category',
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='subcategory',
            field=models.ForeignKey(default=1, to='stakeholders.SubCategory', null=True),
        ),
    ]
