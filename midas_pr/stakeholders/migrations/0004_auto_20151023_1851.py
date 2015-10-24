# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholders', '0003_auto_20151023_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stakeholder',
            old_name='christmas_invite',
            new_name='christmas_card',
        ),
    ]
