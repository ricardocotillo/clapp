from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class UserComment(models.Model):
    sender = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='user_comments'
    )
    receiver = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    message = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)


class ClubComment(models.Model):
    sender = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='team_comments'
    )
    receiver = models.ForeignKey(
        'club.Club',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    message = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)


class MatchComment(models.Model):
    sender = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='match_comments'
    )
    receiver = models.ForeignKey(
        'match.Match',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    message = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    rating = models.FloatField(
        validators=(
            MaxValueValidator(limit_value=5),
            MinValueValidator(limit_value=1),
        ),
    )
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='rates'
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        indexes = (
            models.Index(
                fields=('content_type', 'object_id',),
            ),
        )
