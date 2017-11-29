# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('telegram_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20, blank=True, null=True)),
                ('station', models.CharField(max_length=20, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(unique=True)),
                ('text', models.TextField()),
                ('place_list', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('shortname', models.CharField(max_length=20)),
                ('metro', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('person', models.ForeignKey(to='PicketAdminApp.Person')),
                ('picket', models.ForeignKey(to='PicketAdminApp.Picket')),
                ('place', models.ForeignKey(to='PicketAdminApp.Place')),
            ],
        ),
    ]
