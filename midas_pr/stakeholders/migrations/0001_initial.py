# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(default=b'Not Set', unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CommunicationPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preference_name', models.CharField(default=b'Not Set', unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MidasOffice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office_name', models.CharField(default=b'N/A', unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('spouse', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('phone_work', models.CharField(max_length=200)),
                ('phone_mobile', models.CharField(max_length=200)),
                ('phone_fax', models.CharField(max_length=200)),
                ('phone_home', models.CharField(max_length=200)),
                ('email_work', models.EmailField(max_length=254)),
                ('email_home', models.EmailField(max_length=254)),
                ('url', models.URLField()),
                ('work_address1', models.CharField(max_length=200)),
                ('work_address2', models.CharField(max_length=200)),
                ('work_address_city', models.CharField(max_length=200)),
                ('work_address_state', models.CharField(max_length=200)),
                ('work_address_zip', models.CharField(max_length=200)),
                ('work_address_country', models.CharField(max_length=200)),
                ('home_address1', models.CharField(max_length=200)),
                ('home_address_city', models.CharField(max_length=200)),
                ('home_address_state', models.CharField(max_length=200)),
                ('home_address_zip', models.CharField(max_length=200)),
                ('home_address_country', models.CharField(max_length=200)),
                ('stakeholder_notes', models.TextField()),
                ('lf_open_house_2012', models.BooleanField()),
                ('ea1_comment', models.BooleanField()),
                ('ea1_positive', models.NullBooleanField()),
                ('ea1_topic_1', models.CharField(max_length=200)),
                ('ea1_topic_2', models.CharField(max_length=200)),
                ('ea1_topic_3', models.CharField(max_length=200)),
                ('ea1_format', models.CharField(max_length=200)),
                ('ea2_email', models.BooleanField()),
                ('ea2_letter', models.BooleanField()),
                ('ea2_rp', models.CharField(max_length=200)),
                ('ea2_comment', models.BooleanField()),
                ('ea2_positive', models.NullBooleanField()),
                ('ea2_topic_1', models.CharField(max_length=200)),
                ('ea2_topic_2', models.CharField(max_length=200)),
                ('ea2_topic_3', models.CharField(max_length=200)),
                ('ea2_format', models.CharField(max_length=200)),
                ('ea3_outreach', models.BooleanField()),
                ('ea3_rp', models.CharField(max_length=200)),
                ('contacted', models.BooleanField()),
                ('ea3_email', models.BooleanField()),
                ('ea3_letter', models.BooleanField()),
                ('site_tour_date', models.DateField()),
                ('tour_group', models.CharField(max_length=200)),
                ('lf_open_house_2013', models.BooleanField()),
                ('category', models.ForeignKey(to='stakeholders.Category')),
                ('communication_preference', models.ForeignKey(to='stakeholders.CommunicationPreference')),
                ('midas_office', models.ForeignKey(to='stakeholders.MidasOffice')),
            ],
        ),
        migrations.CreateModel(
            name='StakeholderGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(default=b'Not Set', unique=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='stakeholder_group',
            field=models.ForeignKey(to='stakeholders.StakeholderGroup'),
        ),
    ]
