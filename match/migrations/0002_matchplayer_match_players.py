# Generated by Django 4.2.3 on 2023-08-01 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('local', 'Local'), ('visitor', 'Visitor')], max_length=15)),
                ('assisted', models.BooleanField(null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_players', to='match.match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_matches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='players',
            field=models.ManyToManyField(related_name='matches', through='match.MatchPlayer', to=settings.AUTH_USER_MODEL),
        ),
    ]