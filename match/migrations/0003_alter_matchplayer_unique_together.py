# Generated by Django 4.2.3 on 2023-08-01 23:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('match', '0002_matchplayer_match_players'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='matchplayer',
            unique_together={('match', 'user')},
        ),
    ]