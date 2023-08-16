# Generated by Django 4.2.3 on 2023-08-16 05:00

import datetime
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='days',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], unique=True, validators=[django.core.validators.MaxValueValidator(limit_value=7), django.core.validators.MinValueValidator(limit_value=1)]), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='court',
            name='end',
            field=models.TimeField(default=datetime.time(23, 0)),
        ),
        migrations.AlterField(
            model_name='court',
            name='start',
            field=models.TimeField(default=datetime.time(8, 0)),
        ),
    ]
