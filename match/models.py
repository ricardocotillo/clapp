from django.db import models


class Match(models.Model):
    local = models.ForeignKey(
        'club.Club',
        on_delete=models.CASCADE,
        related_name='matches_as_local',
    )
    visitor = models.ForeignKey(
        'club.Club',
        on_delete=models.CASCADE,
        related_name='matches_as_visitor',
    )
    referees = models.ManyToManyField(
        'authentication.User',
        related_name='matches_observed',
    )
    datetime = models.DateTimeField()
    address = models.CharField(max_length=300)
    # solo arbitro puede determinar a ganador
    winner = models.ForeignKey(
        'club.Club',
        on_delete=models.CASCADE,
        related_name='matches_won',
    )
    players = models.ManyToManyField(
        'authentication.User',
        through='MatchPlayer',
        related_name='matches',
    )


class MatchPlayer(models.Model):
    class MatchPlayerTypes(models.TextChoices):
        LOCAL = 'local', 'Local'
        VISITOR = 'visitor', 'Visitor'

    match = models.ForeignKey(
        'Match',
        on_delete=models.CASCADE,
        related_name='match_players',
    )
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='match_players',
    )
    type = models.CharField(
        max_length=15,
        choices=MatchPlayerTypes.choices,
    )
    assisted = models.BooleanField(
        null=True
    )

    class Meta:
        unique_together = ('match', 'user',)
