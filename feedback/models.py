from django.db import models


class UserComment(models.Model):
    sender = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='user_comments'
    )
    receiver = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='comments_received'
    )
    message = models.TextField(max_length=300)


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
