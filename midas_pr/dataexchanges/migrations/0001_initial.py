# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import midas_pr.dataexchanges.models


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalTracking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_data_name', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('purpose_of_data_exchange', models.CharField(max_length=200)),
                ('datasets', models.TextField(blank=True)),
                ('approved', models.NullBooleanField()),
                ('approved_by', models.ManyToManyField(related_name='approved_by', to='stakeholders.Stakeholder')),
                ('cc', models.ManyToManyField(related_name='cc', to='stakeholders.Stakeholder')),
                ('from_1', models.ForeignKey(related_name='from_1', to='stakeholders.Stakeholder')),
                ('third_party_organization_to_receive_data', models.ForeignKey(to='stakeholders.StakeholderGroup')),
                ('third_party_requested_to_receive_data', models.ForeignKey(related_name='third_party_requested_to_receive_data', default=1439, to='stakeholders.Stakeholder')),
                ('to', models.ManyToManyField(related_name='to', to='stakeholders.Stakeholder')),
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
                ('document_data_name', models.CharField(max_length=200)),
                ('document_data_type', models.CharField(max_length=200, blank=True)),
                ('date_sent_received', models.DateField(default=django.utils.timezone.now)),
                ('purpose', models.CharField(max_length=200, blank=True)),
                ('approved', models.NullBooleanField()),
                ('description', models.CharField(max_length=200, blank=True)),
                ('response_required', models.BooleanField(default=False)),
                ('response_due_date', models.DateField(default=midas_pr.dataexchanges.models.duedate)),
                ('comments', models.TextField(blank=True)),
                ('data_saved_as', models.TextField(blank=True)),
                ('attachments', models.FileField(upload_to=b'attachments', blank=True)),
                ('category', models.ForeignKey(default=1, to='dataexchanges.Category')),
                ('mg_employee_assigned', models.ForeignKey(related_name='mg_employee_assigned', default=1439, to='stakeholders.Stakeholder')),
                ('third_party_name', models.ForeignKey(default=1439, to='stakeholders.Stakeholder')),
                ('third_party_organization', models.ForeignKey(to='stakeholders.StakeholderGroup')),
            ],
        ),
    ]
