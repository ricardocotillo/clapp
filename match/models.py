from typing import Collection, Optional
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericRelation


class Match(models.Model):
    clubs = models.ManyToManyField(
        'club.Club',
        related_name='matches',
        through='match.MatchClub',
    )
    referees = models.ManyToManyField(
        'authentication.User',
        related_name='matches_observed',
    )
    datetime = models.DateTimeField()
    address = models.CharField(max_length=300)
    comments = GenericRelation(
        'feedback.Comment',
        related_query_name='match'
    )


class MatchClub(models.Model):
    match = models.ForeignKey(
        'Match', on_delete=models.CASCADE, related_name='match_clubs')
    club = models.ForeignKey('club.Club', on_delete=models.CASCADE)
    won = models.BooleanField(default=False)
    players = models.ManyToManyField(
        'authentication.User',
        related_name='match_clubs',
        through='MatchClubUser'
    )

    def clean_fields(self, exclude: Collection[str] | None = ...) -> None:
        super().clean_fields(exclude)
        wmatch = self.match.match_clubs.filter(won=True).first()
        if wmatch and wmatch.pk != self.pk and self.won:
            raise ValidationError({
                'won': 'Solo un ganador por partido es permitido.',
            })

    def clean(self) -> None:
        if self.match.clubs.count() >= 2 and not self.pk:
            raise ValidationError('Solo dos clubes son permitidos por partido')
        return super().clean()


class MatchClubUser(models.Model):
    match_club = models.ForeignKey(MatchClub, on_delete=models.CASCADE)
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    assited = models.BooleanField(null=True)
