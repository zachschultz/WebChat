# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0013_auto_20150424_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='post_date',
            field=models.DateTimeField(verbose_name='date posted', default=datetime.datetime(2015, 4, 24, 10, 16, 27, 509462, tzinfo=utc)),
        ),
    ]
