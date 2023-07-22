from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # jugador, organizador, arbitro, admin de cancha
    image = models.ImageField(null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, default='player')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username',)
