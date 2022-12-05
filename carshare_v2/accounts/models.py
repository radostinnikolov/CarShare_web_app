from django.contrib.auth import models as auth_models
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from carshare_v2.accounts.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class Profile(models.Model):
    MAX_LEN_FIRST_NAME = 50
    MAX_LEN_LAST_NAME = 50
    MIN_LEN_FIRST_NAME = 2
    MIN_LEN_LAST_NAME = 2
    MIN_AGE = 0
    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_FIRST_NAME),
        ),
        null=False,
        blank=False
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_LAST_NAME),
        ),
        null=False,
        blank=False
    )
    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(MIN_AGE),
        ),
        null=True,
        blank=True
    )

    profile_picture = models.ImageField(
        default='images/Default-welcomer.png',
        upload_to='images',
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
