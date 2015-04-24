# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20150421_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 9, 44, 37, 555462, tzinfo=utc), verbose_name='date posted'),
        ),
    ]
