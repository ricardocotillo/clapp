from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # jugador, organizador, arbitro, admin de cancha
    image = models.ImageField(null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, default='player')
    rating = models.FloatField(
        validators=(
            MaxValueValidator(limit_value=5),
            MinValueValidator(limit_value=1),
        ),
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username',)
