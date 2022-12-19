import datetime

from django.core.exceptions import ValidationError


def validate_date_is_not_in_the_past(value):
    if value < datetime.date.today():
        raise ValidationError('The date cannot be in the past!')

def validate_chatroom_name_contains_only_letters_or_digits(value):
    if not value.isalnum():
        raise ValidationError('Chatroom name must contain only letters and/or numbers!')