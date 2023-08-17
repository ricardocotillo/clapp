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
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        indexes = (
            models.Index(
                fields=('content_type', 'object_id',),
            ),
        )


class Image(models.Model):
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField()
    description = models.TextField(null=True, max_length=150)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        indexes = (
            models.Index(
                fields=('content_type', 'object_id',),
            ),
        )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        if not self.description:
            self.description = None
        return super().save(force_insert, force_update, using, update_fields)
