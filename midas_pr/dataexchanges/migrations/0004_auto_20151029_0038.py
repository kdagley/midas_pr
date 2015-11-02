# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataexchanges', '0003_auto_20151025_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvaltracking',
            name='approved_by',
            field=models.ForeignKey(related_name='approved_by', default=1, to='stakeholders.Stakeholder'),
        ),
        migrations.AlterField(
            model_name='approvaltracking',
            name='approved_by_2',
            field=models.ForeignKey(related_name='approved_by_2', default=1, to='stakeholders.Stakeholder'),
        ),
        migrations.AlterField(
            model_name='approvaltracking',
            name='cc',
            field=models.ForeignKey(related_name='cc', default=1, to='stakeholders.Stakeholder'),
        ),
        migrations.AlterField(
            model_name='approvaltracking',
            name='from_1',
            field=models.ForeignKey(related_name='from_1', default=1, to='stakeholders.Stakeholder'),
        ),
        migrations.AlterField(
            model_name='approvaltracking',
            name='third_party_requested_to_receive_data',
            field=models.ForeignKey(related_name='third_party_requested_to_receive_data', default=1, to='stakeholders.Stakeholder'),
        ),
        migrations.AlterField(
            model_name='approvaltracking',
            name='to',
            field=models.ForeignKey(related_name='to', default=1, to='stakeholders.Stakeholder'),
        ),
        migrations.AlterField(
            model_name='report',
            name='category',
            field=models.ForeignKey(to='dataexchanges.Category', null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='mg_employee_assigned',
            field=models.ForeignKey(related_name='mg_employee_assigned', default=1, to='stakeholders.Stakeholder'),
        ),
    ]
