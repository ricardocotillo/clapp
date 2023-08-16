from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation


class User(AbstractUser):
    # jugador, organizador, arbitro, admin de cancha
    class Role(models.TextChoices):
        PLAYER = 'player', 'Jugador'
        ORGANIZER = 'organizer', 'Organizador'
        REFEREE = 'referee', 'Arbitro'
        ADMIN = 'admin', 'Administrador'
    image = models.ImageField(null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PLAYER
    )
    ratings = GenericRelation('feedback.Rating', related_query_name='user')
    comments = GenericRelation('feedback.Comment', related_query_name='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username',)
