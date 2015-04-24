# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20150423_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 11, 53, 57, 32261, tzinfo=utc), verbose_name='date posted'),
        ),
    ]
