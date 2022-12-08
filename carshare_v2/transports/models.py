from enum import Enum

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from carshare_v2.common.models import City

UserModel = get_user_model()


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Statuses(ChoicesEnum):
    ACTIVE = 'Active'
    FINISHED = 'Finished'


class Transport(models.Model):
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='from_city',
        related_query_name='from_city',
        null=False,
        blank=False
    )
    to_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='to_city',
        related_query_name='to_city',
        null=False,
        blank=False
    )
    driver = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        related_name='driver',
        related_query_name='driver',
        null=False,
        blank=False
    )
    passengers = models.ManyToManyField(
        UserModel,
        related_name='passengers',
        related_query_name='passengers',
        blank=True,
    )
    requests = models.ManyToManyField(
        UserModel,
        related_name='requests',
        related_query_name='requests',
        blank=True
    )
    date = models.DateField(
        null=False,
        blank=False
    )
    time = models.TimeField(
        default='Not set',
        null=True,
        blank=True
    )
    description = models.CharField(
        max_length=300,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=Statuses.choices(),
        default='Active',
        null=False,
        blank=False
    )
    total_seats = models.IntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(6)
        ),
        null=False,
        blank=False
    )
    chatroom_name = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
