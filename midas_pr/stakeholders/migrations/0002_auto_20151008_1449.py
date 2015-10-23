# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default=b'Unknown', unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='communicationpreference',
            name='preference_name',
            field=models.CharField(default=b'None', unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='midasoffice',
            name='office_name',
            field=models.CharField(default=b'None', unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='category',
            field=models.ForeignKey(default=1, to='stakeholders.Category', null=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='communication_preference',
            field=models.ForeignKey(default=1, to='stakeholders.CommunicationPreference', null=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='contacted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea1_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea1_format',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea1_topic_1',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea1_topic_2',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea1_topic_3',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea2_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea2_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea2_format',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea2_letter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea2_rp',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea2_topic_1',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea2_topic_2',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea2_topic_3',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea3_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea3_letter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea3_outreach',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='ea3_rp',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='email_home',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='email_work',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='first_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='home_address1',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='home_address_city',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='home_address_country',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='home_address_state',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='home_address_zip',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='last_name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='lf_open_house_2012',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='lf_open_house_2013',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='midas_office',
            field=models.ForeignKey(default=1, to='stakeholders.MidasOffice', null=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='phone_fax',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='phone_home',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='phone_mobile',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='phone_work',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='site_tour_date',
            field=models.DateField(default=datetime.date(2000, 1, 1)),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='spouse',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='stakeholder_group',
            field=models.ForeignKey(default=1, to='stakeholders.StakeholderGroup', null=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='stakeholder_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='title',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='tour_group',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='work_address1',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='work_address2',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='work_address_city',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='work_address_country',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='work_address_state',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='work_address_zip',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholdergroup',
            name='group_name',
            field=models.CharField(default=b'Unknown', unique=True, max_length=200),
        ),
    ]
