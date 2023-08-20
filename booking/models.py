import datetime
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import timedelta
from authentication.models import User


class Place(models.Model):
    owner = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='places',
    )
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=250)
    district = models.CharField(max_length=6)
    city = models.CharField(max_length=5)
    province = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    long = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    images = GenericRelation(
        'feedback.Image',
        related_query_name='place',
    )

    def __str__(self) -> str:
        return self.name


class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pendiente'
        CONFIRMED = 'confirmed', 'Confirmado'
        CANCELED = 'canceled', 'Canceledo'

    court = models.ForeignKey(
        'Court',
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self) -> str:
        return f'{self.court.name} - {self.start} - {self.status}'


class Court(models.Model):
    def default_week_days(self):
        return [1, 2, 3, 4, 5, 6, 7]

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
    duration = models.DurationField(default=timedelta(hours=1))
    week_days = ArrayField(
        models.PositiveIntegerField(
            choices=Day.choices,
            unique=True,
            validators=(
                MaxValueValidator(limit_value=7),
                MinValueValidator(limit_value=1),
            ),
        ),
        default=default_week_days
    )
    days = models.PositiveIntegerField(default=7)
    start = models.TimeField(default=datetime.time(8, 0, 0))
    end = models.TimeField(default=datetime.time(23, 0, 0))
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    sport = models.ForeignKey(
        'club.Sport',
        on_delete=models.SET_NULL,
        null=True,
        related_name='courts',
    )

    class Meta:
        unique_together = ('place_id', 'name',)

    def __str__(self) -> str:
        return self.name

    def book(self, user: User, start: datetime, duration: timedelta):
        return Booking.objects.create(
            court_id=self.pk,
            user=user,
            start=start,
            end=start + duration,
        )
