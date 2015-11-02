# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholder',
            name='allow_data_exchange',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='communication_preference',
            field=models.ForeignKey(to='stakeholders.CommunicationPreference', null=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='midas_office',
            field=models.ForeignKey(to='stakeholders.MidasOffice', null=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='stakeholder_group',
            field=models.ForeignKey(verbose_name=b'organization', to='stakeholders.StakeholderGroup', null=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='subcategory',
            field=models.ForeignKey(to='stakeholders.SubCategory', null=True),
        ),
    ]
