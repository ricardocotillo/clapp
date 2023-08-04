# Generated by Django 4.2.3 on 2023-08-04 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('match', '0003_alter_matchplayer_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchplayer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_players', to=settings.AUTH_USER_MODEL),
        ),
    ]