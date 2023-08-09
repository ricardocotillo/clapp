from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


class Sport(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self) -> str:
        return self.name


class Club(models.Model):
    sport = models.ForeignKey(
        'club.Sport',
        on_delete=models.SET_NULL,
        null=True,
        related_name='clubs',
    )
    owner = models.ForeignKey(
        'authentication.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='owned_clubs',
    )
    name = models.CharField(max_length=100, unique=True, verbose_name='nombre')
    logo = models.ImageField(null=True)
    members = models.ManyToManyField(
        'authentication.User',
        related_name='clubs',
        through='club.Membership',
    )
    ratings = GenericRelation('feedback.Rating', related_query_name='club')
    comments = GenericRelation('feedback.Comment', related_query_name='club')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Membership(models.Model):
    class Roles(models.TextChoices):
        OWNER = 'owner', 'Creador'
        ADMIN = 'admin', 'Administrador'
        MEMBER = 'member', 'Miembro'

    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    club = models.ForeignKey('club.Club', on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.MEMBER,
    )
    team = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.club.name} - {self.member.email} - {self.role}'


class ClubImage(models.Model):
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name='images'
    )
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField()
    description = models.TextField(null=True)
