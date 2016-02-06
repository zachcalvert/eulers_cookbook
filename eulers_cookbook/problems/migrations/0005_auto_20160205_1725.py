# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_problem_interactive_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.CharField(max_length=800),
        ),
    ]
