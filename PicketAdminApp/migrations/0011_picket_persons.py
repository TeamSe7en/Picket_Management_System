# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PicketAdminApp', '0010_picket_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='picket',
            name='persons',
            field=models.ManyToManyField(to='PicketAdminApp.Person'),
        ),
    ]
