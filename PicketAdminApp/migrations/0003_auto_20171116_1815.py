# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PicketAdminApp', '0002_metrostation_person_picket_place_spot'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='shortname',
            field=models.CharField(max_length=20, default='sn'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picket',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
