# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PicketAdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metrostation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('telegram_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20)),
                ('station', models.ForeignKey(to='PicketAdminApp.Metrostation')),
            ],
        ),
        migrations.CreateModel(
            name='Picket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
                ('metro', models.ForeignKey(to='PicketAdminApp.Metrostation')),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('person', models.ForeignKey(to='PicketAdminApp.Person')),
                ('place', models.ForeignKey(to='PicketAdminApp.Place')),
            ],
        ),
    ]
