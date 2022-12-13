from django.db import models


class City(models.Model):
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    CITY_MAX_LEN = 30
    name = models.CharField(
        max_length=CITY_MAX_LEN,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name
