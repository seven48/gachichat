""" Users module models """

from django.db import models

# from rooms.models import Room
from users.manager import UserManager


class UserProfile(models.Model):
    """ UserProfile model """

    first_name = models.CharField(
        max_length=32
    )
    last_name = models.CharField(
        max_length=32
    )
    room = models.ForeignKey(
        'rooms.Room',
        models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of user registration'
    )
    last_active = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of user last activity'
    )
    active = models.BooleanField(
        default=True,
        verbose_name='Is the user is available'
    )

    objects = UserManager()
