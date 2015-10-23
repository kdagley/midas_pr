# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0002_auto_20151008_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholder',
            name='christmas_invite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='stakeholder_group',
            field=models.ForeignKey(default=1, verbose_name=b'organization', to='stakeholders.StakeholderGroup', null=True),
        ),
    ]
