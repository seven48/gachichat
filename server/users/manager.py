import requests
import jwt
from django.db import models
from django.utils import timezone

from engine.serializer import to_json
from server.settings import SECRET_KEY, USER_TOKEN_EXPIRING
from engine.exceptions import APITokenError


class UserManager(models.Manager):
    """ Manager for user profiles """
    def new_user(self, room):
        """ Creates new user and returns JWT with user data """
        first_name, last_name = self.get_random_name()
        user = self.create(
            first_name=first_name,
            last_name=last_name,
            room=room
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
        response = to_json(user)
        response['token'] = token.decode('UTF-8')
        response['expired_in'] = expired_in
        return response

    def decode_token(self, token):
        """ Decodes JWT and returns found user """
        try:
            payload = jwt.decode(token, SECRET_KEY)
        except jwt.DecodeError:
            raise APITokenError()
        else:
            now = int(timezone.now().timestamp())
            if now > payload['expired_in']:
                raise APITokenError('Token expired')
            user = self.filter(id=payload['user_id']).first()
            if not user:
                raise APITokenError('User is not found')
            if not user.active:
                raise APITokenError('User is not active')
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
