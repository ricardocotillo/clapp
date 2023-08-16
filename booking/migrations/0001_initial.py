# Generated by Django 4.2.3 on 2023-08-15 22:54

import datetime
from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0002_delete_clubimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('address', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=5)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to=settings.AUTH_USER_MODEL)),
                ('sports', models.ManyToManyField(related_name='places', to='club.sport')),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('days', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], unique=True, validators=[django.core.validators.MaxValueValidator(limit_value=7), django.core.validators.MinValueValidator(limit_value=1)]), size=None)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courts', to='booking.place')),
            ],
            options={
                'unique_together': {('place_id', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending', max_length=15)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='booking.court')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
