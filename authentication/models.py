from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation


class User(AbstractUser):
    # organizador, arbitro, admin de cancha
    class Role(models.TextChoices):
        ORGANIZER = 'organizer', 'Organizador'
        REFEREE = 'referee', 'Arbitro'
        ADMIN = 'admin', 'Administrador'

    image = models.ImageField(null=True)
    email = models.EmailField(unique=True)
    ratings = GenericRelation('feedback.Rating', related_query_name='user')
    comments = GenericRelation('feedback.Comment', related_query_name='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username',)
