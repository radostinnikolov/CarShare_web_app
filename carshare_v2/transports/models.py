import datetime
from enum import Enum

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save

from carshare_v2.common.models import City
from carshare_v2.transports.signals import clear_cache
from carshare_v2.transports.validators import validate_date_is_not_in_the_past

UserModel = get_user_model()





class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Statuses(ChoicesEnum):
    ACTIVE = 'Active'
    FINISHED = 'Finished'


class Transport(models.Model):
    MAX_LEN_DESCR = 300
    MAX_LEN_STATUS = 20
    MIN_VALUE_SEATS = 1
    MAX_VALUE_SEATS = 6
    MAX_LEN_CHATROOM = 20
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
        on_delete=models.CASCADE,
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
        validators=(
            validate_date_is_not_in_the_past,
        ),
        null=False,
        blank=False

    )
    time = models.TimeField(
        null=True,
        blank=True
    )
    description = models.CharField(
        max_length=MAX_LEN_DESCR,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=MAX_LEN_STATUS,
        choices=Statuses.choices(),
        default='ACTIVE',
        null=False,
        blank=False
    )
    total_seats = models.IntegerField(
        validators=(
            MinValueValidator(MIN_VALUE_SEATS),
            MaxValueValidator(MAX_VALUE_SEATS)
        ),
        null=False,
        blank=False
    )
    chatroom_name = models.CharField(
        max_length=MAX_LEN_CHATROOM,
        null=True,
        blank=True
    )
    post_save.connect(clear_cache)

    def clean(self):
        if self.from_city_id == self.to_city_id:
            raise ValidationError('"From city" and "To city" fields must be be different.')


