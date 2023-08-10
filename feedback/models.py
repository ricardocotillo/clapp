from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    owner = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='sent_comments'
    )
    message = models.TextField(max_length=300)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = (
            models.Index(
                fields=('content_type', 'object_id'),
            ),
        )


class Rating(models.Model):
    owner = models.ForeignKey(
        'authentication.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='ratings'
    )
    rating = models.FloatField(
        validators=(
            MaxValueValidator(limit_value=5),
            MinValueValidator(limit_value=1),
        ),
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
