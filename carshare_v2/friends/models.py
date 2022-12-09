from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class FriendRequest(models.Model):
    requester = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='requester',
        related_query_name='requester'
    )
    receiver = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='receiver',
        related_query_name='receiver'
    )
    def __str__(self):
        return f'From user: {self.requester} - To user: {self.receiver}'


class Friend(models.Model):
    requester = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='requester_friend',
        related_query_name='requester_friend'
    )
    receiver = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='receiver_friend',
        related_query_name='receiver_friend'
    )
    def __str__(self):
        return f'From user: {self.requester} - To user: {self.receiver}'
