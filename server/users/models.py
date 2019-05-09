""" Users module models """


import requests
import jwt
from django.db import models
from django.utils import timezone

from server.settings import SECRET_KEY, USER_TOKEN_EXPIRING


class UserManager(models.Manager):
    """ Manager for user profiles """
    def new_user(self):
        """ Creates new user and returns JWT with user data """
        first_name, last_name = self.get_random_name()
        user = self.create(
            first_name=first_name,
            last_name=last_name
        )
        created = int(timezone.now().timestamp())
        expired_in = created + USER_TOKEN_EXPIRING
        payload = {}
        payload['user_id'] = user.id
        payload['created'] = created
        payload['expired_in'] = expired_in
        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
        return {
            'token': token.decode('UTF-8'),
            'created': created,
            'expired_in': expired_in,
            'first_name': first_name,
            'last_name': last_name
        }

    def decode_token(self, token):
        """ Decodes JWT and returns found user """
        try:
            payload = jwt.decode(token, SECRET_KEY)
        except jwt.DecodeError:
            raise Exception('Token is not valid')
        else:
            now = int(timezone.now().timestamp())
            if now > payload['expired_in']:
                raise Exception('Token expired')
            user = self.filter(id=payload['user_id']).first()
            if not user:
                raise Exception('User is not found')
            if not user.active:
                raise Exception('User is not active')
            return user

    @staticmethod
    def get_random_name():
        """ Generates random first and last name """
        data = requests.get('https://randomuser.me/api/')
        results = data.json()['results'].pop()
        return [
            results['name']['first'],
            results['name']['last']
        ]


class UserProfile(models.Model):
    """ UserProfile model """

    first_name = models.CharField(
        max_length=32
    )
    last_name = models.CharField(
        max_length=32
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
