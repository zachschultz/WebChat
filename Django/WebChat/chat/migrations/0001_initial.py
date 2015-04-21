# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('highlighted', models.TextField()),
                ('creator', models.CharField(max_length=15, default='Anonymous')),
                ('content', models.CharField(max_length=200)),
                ('post_date', models.DateTimeField(verbose_name='date posted', default=datetime.datetime(2015, 4, 21, 15, 51, 36, 733227, tzinfo=utc))),
                ('owner', models.ForeignKey(related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
