# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_auto_20150423_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='post_date',
            field=models.DateTimeField(verbose_name='date posted', default=datetime.datetime(2015, 4, 23, 15, 41, 37, 621450, tzinfo=utc)),
        ),
    ]
