# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PicketAdminApp', '0003_auto_20171116_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='patronymic',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='station',
            field=models.ForeignKey(null=True, to='PicketAdminApp.Metrostation'),
        ),
    ]
