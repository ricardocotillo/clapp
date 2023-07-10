from django.db import models


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
