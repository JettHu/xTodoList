# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('todo', models.CharField(max_length=50)),
                ('desc', models.TextField(default=b'', blank=True)),
                ('done', models.BooleanField(default=False)),
                ('priority', models.IntegerField(default=0)),
                ('expire', models.BooleanField(default=False)),
                ('expire_date', models.DateTimeField(null=True, blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('done', 'priority', 'add_time'),
            },
        ),
    ]
