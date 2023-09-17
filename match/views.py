from rest_framework import viewsets
from django.core.mail import send_mail
from club.models import Club, Membership
from .models import Match, MatchClub, MatchClubUser


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()

    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)
        challenger: Club = self.object.clubs.get(challenger=True)
        challenged: Club = self.object.clubs.get(challenger=False)
        admins_emails = list(Membership.objects.filter(
            clubs=challenged,
            role=Membership.Roles.ADMIN,
        ).values_list('user__email', flat=True))
        send_mail(
            'Te ha llegado un nuevo reto',
            f'El Club {challenger.name} te ha retado\nFecha y hora: {self.object.datetime}\nDirección: {self.object.address}',
            recipient_list=admins_emails,
            fail_silently=True,
        )
        return res
