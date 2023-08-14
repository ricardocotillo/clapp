from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField


class Place(models.Model):
    owner = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='places',
    )
    name = models.CharField(max_length=150)
    address = models.CharField()
    district = models.CharField()
    city = models.CharField()
    sports = models.ManyToManyField(
        'club.Sports',
        related_name='places',
    )


class Court(models.Model):
    class Day(models.IntegerChoices):
        MONDAY = 1, 'Monday'
        TUESDAY = 2, 'Tuesday'
        WEDNESDAY = 3, 'Wednesday'
        THURSDAY = 4, 'Thursday'
        FRIDAY = 5, 'Friday'
        SATURDAY = 6, 'Saturday'
        SUNDAY = 7, 'Sunday'

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='courts',
    )
    name = models.CharField(max_length=100)
    images = GenericRelation(
        'feedback.Image',
        related_query_name='court',
    )
    block = models.DurationField()
    days = ArrayField(
        models.PositiveIntegerField(
            choices=Day.choices,
            unique=True,
            validators=(
                MaxValueValidator(limit_value=7),
                MinValueValidator(limit_value=1),
            ),
        ),
    )
    start = models.TimeField()
    end = models.TimeField()
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )


class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELED = 'canceled', 'Canceled'

    court = models.ForeignKey(
        Court,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
    )