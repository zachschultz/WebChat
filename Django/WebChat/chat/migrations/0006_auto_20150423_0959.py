# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20150423_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 9, 59, 49, 836182, tzinfo=utc), verbose_name='date posted'),
        ),
    ]
