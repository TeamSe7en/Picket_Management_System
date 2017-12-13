# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PicketAdminApp', '0009_task_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='picket',
            name='places',
            field=models.ManyToManyField(to='PicketAdminApp.Place'),
        ),
    ]
