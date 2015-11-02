# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import midas_pr.dataexchanges.models


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0002_auto_20151025_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalTracking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_data_name', models.CharField(max_length=200, blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('purpose_of_data_exchange', models.CharField(max_length=200, blank=True)),
                ('datasets', models.TextField(blank=True)),
                ('approved', models.NullBooleanField()),
                ('field1', models.CharField(max_length=200, blank=True)),
                ('approved_by', models.ForeignKey(related_name='approved_by', to='stakeholders.Stakeholder', null=True)),
                ('approved_by_2', models.ForeignKey(related_name='approved_by_2', to='stakeholders.Stakeholder', null=True)),
                ('cc', models.ForeignKey(related_name='cc', to='stakeholders.Stakeholder', null=True)),
                ('from_1', models.ForeignKey(related_name='from_1', to='stakeholders.Stakeholder', null=True)),
                ('third_party_requested_to_receive_data', models.ForeignKey(related_name='third_party_requested_to_receive_data', to='stakeholders.Stakeholder', null=True)),
                ('to', models.ForeignKey(related_name='to', to='stakeholders.Stakeholder', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_data_name', models.CharField(max_length=200, blank=True)),
                ('document_data_type', models.CharField(max_length=200, blank=True)),
                ('date_sent_received', models.DateField(default=django.utils.timezone.now)),
                ('purpose', models.CharField(max_length=200, blank=True)),
                ('approved', models.NullBooleanField()),
                ('description', models.CharField(max_length=200, blank=True)),
                ('response_required', models.BooleanField(default=False)),
                ('response_due_date', models.DateField(default=midas_pr.dataexchanges.models.duedate)),
                ('comments', models.TextField(blank=True)),
                ('data_saved_as', models.TextField(blank=True)),
                ('attachments', models.CharField(max_length=200, blank=True)),
                ('category', models.ForeignKey(default=1, to='dataexchanges.Category', null=True)),
                ('mg_employee_assigned', models.ForeignKey(related_name='mg_employee_assigned', to='stakeholders.Stakeholder', null=True)),
                ('third_party_name', models.ForeignKey(related_name='third_party_name', to='stakeholders.Stakeholder', null=True)),
                ('third_party_name_2', models.ForeignKey(related_name='third_party_name_2', to='stakeholders.Stakeholder', null=True)),
                ('third_party_name_3', models.ForeignKey(related_name='third_party_name_3', to='stakeholders.Stakeholder', null=True)),
            ],
        ),
    ]
