import random
import requests
from uuid import uuid4
from django_seed import Seed
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import Group

from authentication.models import User
from club.models import Club, Membership
from utils.models import Sport
from booking.models import Place, Court
from feedback.models import Image
from publications.models import Publication


def get_unsplash_image(q='', page=1) -> str:
    res = requests.get(
        f'{settings.UNSPLASH_BASE}/search/photos/?query={q}&orientation=squarish&page={page}&per_page=1&client_id={settings.UNSPLASH_ACCESS_KEY}'
    )
    j = res.json()
    results = j.get('results')
    data = results[0]
    img_url = data['urls']['regular']
    return img_url


def get_file_from_url(url=None):
    if not url:
        return None
    tmp = NamedTemporaryFile(delete=True)
    b = requests.get(url, stream=True).raw.read()
    tmp.write(b)
    tmp.flush()
    return File(tmp)


class Command(BaseCommand):
    seeder = Seed.seeder()

    def handle(self, *args, **options):
        for r in User.Role.choices:
            Group.objects.create(
                name=r[0]
            )
        self.seeder.add_entity(User, 200, {
            'image': None,
            'is_staff': False,
            'is_active': True,
            'is_superuser': False,
        })
        self.seeder.execute()
        superman = User.objects.create_superuser(
            'super',
            'super@super.com',
            '123',
            first_name='Super',
            last_name='Man',
        )

        Sport.objects.update_or_create(name='Básquetbol')
        Sport.objects.update_or_create(name='Fútbol')
        Sport.objects.update_or_create(name='Voley')
        Sport.objects.update_or_create(name='Tenis')

        bonilla, _ = Place.objects.get_or_create(
            name='Bonilla',
            defaults={
                'owner': superman,
                'address': 'Av. del Ejercito 890',
                'district': '15074',
                'city': 'Lima',
            }
        )

        for i in range(5):
            img_url = get_unsplash_image('soccer', page=i+1)
            f = get_file_from_url(img_url)
            pic = Image(user=superman, content_object=bonilla)
            pic.save()
            pic.image.save(f'{uuid4()}.jpg', f)
            bonilla.images.add(pic, bulk=False)

        chamochumbi, _ = Place.objects.get_or_create(
            owner=superman,
            name='Chamochumbi',
            address='av. nueva direccion',
            district='15076',
            city='Lima',
        )

        for i in range(5):
            img_url = get_unsplash_image('basketball', page=i+1)
            f = get_file_from_url(img_url)
            pic = Image(user=superman, content_object=chamochumbi)
            pic.save()
            pic.image.save(f'{uuid4()}.jpg', f)
            chamochumbi.images.add(pic, bulk=False)

        Place.objects.create(
            owner=superman,
            name='Chino Vasquez',
            address='av. nueva direccion',
            district='15074',
            city='Lima',
        )

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
                    user_id=u,
                    club_id=c.pk,
                    role=next(roles),
                    team=next(team),
                )

        for i in range(0, 50):
            Publication.objects.create(
                user_id=i+1,
                body=self.seeder.faker.sentence(20)
            )
