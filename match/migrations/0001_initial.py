# Generated by Django 4.2.3 on 2023-08-30 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('address', models.CharField(max_length=300)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_local', to='club.club')),
            ],
        ),
        migrations.CreateModel(
            name='MatchPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('local', 'Local'), ('visitor', 'Visitor')], max_length=15)),
                ('assisted', models.BooleanField(null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_players', to='match.match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_players', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('match', 'user')},
            },
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(related_name='matches', through='match.MatchPlayer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='referees',
            field=models.ManyToManyField(related_name='matches_observed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='visitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_visitor', to='club.club'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_won', to='club.club'),
        ),
    ]
