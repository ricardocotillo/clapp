from django.db import models

class Match(models.Model):
    local = models.ForeignKey('club.Club', on_delete=models.CASCADE, related_name='matches_as_local')
    visitor = models.ForeignKey('club.Club', on_delete=models.CASCADE, related_name='matches_as_visitor')
    referees = models.ManyToManyField('authentication.User', related_name='matches_observed')
    datetime = models.DateTimeField()
    address = models.CharField(max_length=300)
    winner = models.ForeignKey('club.Club', on_delete=models.CASCADE, related_name='matches_won') # solo arbitro puede determinar a ganador