# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_problem_num_inputs'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='interactive_header',
            field=models.CharField(default=b'Enter any number to see it in action!', max_length=80),
        ),
    ]
