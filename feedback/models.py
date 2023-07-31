from django.db import models


class Comment(models.Model):
    sender = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='comments_sent'
    )
    receiver = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='comments_received'
    )
    message = models.TextField(max_length=300)
