# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PicketAdminApp', '0011_picket_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picket',
            name='persons',
            field=models.ManyToManyField(blank=True, null=True, to='PicketAdminApp.Person'),
        ),
        migrations.AlterField(
            model_name='picket',
            name='places',
            field=models.ManyToManyField(blank=True, null=True, to='PicketAdminApp.Place'),
        ),
    ]
