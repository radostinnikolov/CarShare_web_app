from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


UserModel = get_user_model()


class Rating(models.Model):
    to_profile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='receiver_rating',
        related_query_name='receiver_rating',
        null=False,
        blank=False
    )
    from_profile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='giver_rating',
        related_query_name='giver_rating',
        null=False,
        blank=False
    )
    value = models.PositiveIntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(5)
        ),
        null=False,
        blank=False
    )
    def __str__(self):
        return f'From user: {self.from_profile} - To user: {self.to_profile}'