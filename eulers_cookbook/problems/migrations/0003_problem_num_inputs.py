# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_problem_callback_function'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='num_inputs',
            field=models.IntegerField(default=1),
        ),
    ]
