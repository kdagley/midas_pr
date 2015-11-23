# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(default=b'Unknown', unique=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CommunicationPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preference_name', models.CharField(default=b'None', unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MidasOffice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office_name', models.CharField(default=b'None', unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('first_name', models.CharField(max_length=200, blank=True)),
                ('last_name', models.CharField(max_length=200, blank=True)),
                ('spouse', models.CharField(max_length=200, blank=True)),
                ('manage_approvals', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('phone_work', models.CharField(max_length=200, blank=True)),
                ('phone_mobile', models.CharField(max_length=200, blank=True)),
                ('phone_fax', models.CharField(max_length=200, blank=True)),
                ('phone_home', models.CharField(max_length=200, blank=True)),
                ('email_work', models.EmailField(max_length=254, blank=True)),
                ('email_home', models.EmailField(max_length=254, blank=True)),
                ('url', models.URLField(blank=True)),
                ('work_address1', models.CharField(max_length=200, blank=True)),
                ('work_address2', models.CharField(max_length=200, blank=True)),
                ('work_address_city', models.CharField(max_length=200, blank=True)),
                ('work_address_state', models.CharField(max_length=200, blank=True)),
                ('work_address_zip', models.CharField(max_length=200, blank=True)),
                ('work_address_country', models.CharField(max_length=200, blank=True)),
                ('home_address1', models.CharField(max_length=200, blank=True)),
                ('home_address_city', models.CharField(max_length=200, blank=True)),
                ('home_address_state', models.CharField(max_length=200, blank=True)),
                ('home_address_zip', models.CharField(max_length=200, blank=True)),
                ('home_address_country', models.CharField(max_length=200, blank=True)),
                ('stakeholder_notes', models.TextField(blank=True)),
                ('allow_data_exchange', models.BooleanField(default=False)),
                ('christmas_card', models.BooleanField(default=False)),
                ('lf_open_house_2012', models.BooleanField(default=False)),
                ('ea1_comment', models.BooleanField(default=False)),
                ('ea1_positive', models.NullBooleanField()),
                ('ea1_topic_1', models.CharField(max_length=200, blank=True)),
                ('ea1_topic_2', models.CharField(max_length=200, blank=True)),
                ('ea1_topic_3', models.CharField(max_length=200, blank=True)),
                ('ea1_format', models.CharField(max_length=200, blank=True)),
                ('ea2_email', models.BooleanField(default=False)),
                ('ea2_letter', models.BooleanField(default=False)),
                ('ea2_rp', models.CharField(max_length=200, blank=True)),
                ('ea2_comment', models.BooleanField(default=False)),
                ('ea2_positive', models.NullBooleanField()),
                ('ea2_topic_1', models.CharField(max_length=200, blank=True)),
                ('ea2_topic_2', models.CharField(max_length=200, blank=True)),
                ('ea2_topic_3', models.CharField(max_length=200, blank=True)),
                ('ea2_format', models.CharField(max_length=200, blank=True)),
                ('ea3_outreach', models.BooleanField(default=False)),
                ('ea3_rp', models.CharField(max_length=200, blank=True)),
                ('contacted', models.BooleanField(default=False)),
                ('ea3_email', models.BooleanField(default=False)),
                ('ea3_letter', models.BooleanField(default=False)),
                ('site_tour_date', models.DateField(default=datetime.date(2000, 1, 1))),
                ('tour_group', models.CharField(max_length=200, blank=True)),
                ('lf_open_house_2013', models.BooleanField(default=False)),
                ('card_sender', models.ForeignKey(default=1439, to='stakeholders.Stakeholder', null=True)),
                ('communication_preference', models.ForeignKey(to='stakeholders.CommunicationPreference', null=True)),
                ('midas_office', models.ForeignKey(to='stakeholders.MidasOffice', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StakeholderGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(default=b'Unknown', unique=True, max_length=200)),
                ('allow_data_exchange', models.BooleanField(default=False)),
                ('primary_contact', models.ForeignKey(to='stakeholders.Stakeholder', null=True)),
            ],
            options={
                'verbose_name': 'organization',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subcategory_name', models.CharField(default=b'None', max_length=200)),
                ('category', models.ForeignKey(default=1, to='stakeholders.Category', null=True)),
            ],
            options={
                'verbose_name_plural': 'subcategories',
            },
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='stakeholder_group',
            field=models.ForeignKey(verbose_name=b'organization', to='stakeholders.StakeholderGroup', null=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='subcategory',
            field=models.ForeignKey(to='stakeholders.SubCategory', null=True),
        ),
    ]
