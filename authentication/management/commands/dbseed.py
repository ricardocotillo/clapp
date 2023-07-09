import random
from django_seed import Seed
from django.core.management.base import BaseCommand

from authentication.models import User
from club.models import Club, Sport, Membership
from publications.models import Publication


class Command(BaseCommand):
    seeder = Seed.seeder()

    def handle(self, *args, **options):
        self.seeder.add_entity(User, 200, {
            'is_staff': False,
            'is_active': True,
            'is_superuser': False,
        })
        self.seeder.execute()
        User.objects.create_superuser(
            'super',
            'super@super.com',
            '123',
            first_name='Super',
            last_name='Man',
        )

        Sport.objects.update_or_create(name='Básquetbol')
        Sport.objects.update_or_create(name='Fútbol')
        Sport.objects.update_or_create(name='Voley')

        for i in range(0, 10):
            c: Club = Club.objects.create(
                sport_id=random.randint(1, 3),
                name=self.seeder.faker.name()
            )
            start = (i*10) + 1
            stop = start + 20
            users = [u for u in range(start, stop)]
            roles = iter([Membership.Roles.OWNER if r ==
                         0 else Membership.Roles.MEMBER for r in range(0, 20)])
            team = iter([t < 10 for t in range(0, 20)])

            for u in users:
                Membership.objects.create(
                    member_id=u,
                    club_id=c.pk,
                    role=next(roles),
                    team=next(team),
                )

        for i in range(0, 50):
            Publication.objects.create(
                user_id=i+1,
                body=self.seeder.faker.sentence(300)
            )
