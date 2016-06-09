# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20160608_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')], choices=[(b'CSE', 'CSE'), (b'EEE', 'EEE'), (b'ME', 'ME'), (b'CSA', 'CSA'), (b'ECE', 'ECE')], max_length=32, blank=True, null=True, verbose_name='Branch'),
        ),
        migrations.AlterField(
            model_name='user',
            name='aums_id',
            field=models.CharField(max_length=32, unique=True, serialize=False, verbose_name='Aums ID', primary_key=True),
        ),
    ]
