# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PicketAdminApp', '0004_auto_20171116_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='patronymic',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='station',
            field=models.ForeignKey(blank=True, null=True, to='PicketAdminApp.Metrostation'),
        ),
    ]
