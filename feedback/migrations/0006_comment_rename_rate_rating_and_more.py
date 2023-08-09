# Generated by Django 4.2.3 on 2023-08-09 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0005_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=300)),
                ('object_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Rate',
            new_name='Rating',
        ),
        migrations.RemoveField(
            model_name='clubcomment',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='clubcomment',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='matchcomment',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='matchcomment',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='usercomment',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='usercomment',
            name='sender',
        ),
        migrations.RenameIndex(
            model_name='rating',
            new_name='feedback_ra_content_3353c8_idx',
            old_name='feedback_ra_content_7e9908_idx',
        ),
        migrations.DeleteModel(
            name='ClubComment',
        ),
        migrations.DeleteModel(
            name='MatchComment',
        ),
        migrations.DeleteModel(
            name='UserComment',
        ),
        migrations.AddField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['content_type', 'object_id'], name='feedback_co_content_2e5526_idx'),
        ),
    ]
