# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tastypie.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sensor_location', models.CharField(max_length=20)),
                ('entry_date', models.DateTimeField(default=tastypie.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
