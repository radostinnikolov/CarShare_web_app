from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Comment(models.Model):
    COMMENT_MAX_LEN = 200
    to_profile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='commented',
        related_query_name='commented',
        null=False,
        blank=False
    )
    from_profile = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='commenter',
        related_query_name='commenter',
        null=False,
        blank=False
    )
    content = models.CharField(
        max_length=COMMENT_MAX_LEN,
        null=False,
        blank=False
    )
    date_of_publication = models.DateField(
        auto_now_add=True
    )
    def __str__(self):
        return f'From user: {self.from_profile} - To user: {self.to_profile}'