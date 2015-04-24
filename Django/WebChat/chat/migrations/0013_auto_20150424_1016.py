# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_auto_20150423_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='post_date',
            field=models.DateTimeField(verbose_name='date posted', default=datetime.datetime(2015, 4, 24, 10, 16, 4, 998188, tzinfo=utc)),
        ),
    ]
