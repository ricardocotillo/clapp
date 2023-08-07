from django.db import models
from django.utils import timezone
from authentication.models import User


class ReactionType(models.IntegerChoices):
    LIKE = 0, '❤️'


class Reaction(models.Model):
    type = models.IntegerField(choices=ReactionType.choices, null=True)
    user = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='reactions')
    publication = models.ForeignKey(
        'Publication', on_delete=models.CASCADE, related_name='reactions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()


class Publication(models.Model):
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='publications',
    )
    body = models.TextField(max_length=300, null=True)
    image = models.ImageField(null=True)
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.email} - {self.created_at}'

    def react(self, user: User, type: int):
        return Reaction.objects.create(
            type=type,
            user=user,
            publication=self,
        )
