# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0019_auto_20150424_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='post_date',
            field=models.DateTimeField(verbose_name='date posted', default=datetime.datetime(2015, 4, 24, 14, 57, 41, 451824, tzinfo=utc)),
        ),
    ]
