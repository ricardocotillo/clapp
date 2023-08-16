import datetime
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import timedelta


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
    sports = models.ManyToManyField(
        'club.Sport',
        related_name='places',
    )

    def __str__(self) -> str:
        return self.name


class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELED = 'canceled', 'Canceled'

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
    days = ArrayField(
        models.PositiveIntegerField(
            choices=Day.choices,
            unique=True,
            validators=(
                MaxValueValidator(limit_value=7),
                MinValueValidator(limit_value=1),
            ),
        ),
        default=list
    )
    start = models.TimeField(default=datetime.time(8, 0, 0))
    end = models.TimeField(default=datetime.time(23, 0, 0))
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    class Meta:
        unique_together = ('place_id', 'name',)

    def __str__(self) -> str:
        return self.name

    def book(self, user, start: datetime, duration: timedelta):
        return Booking.objects.create(
            court=self.id,
            user=user,
            start=start,
            end=start + duration,
        )
