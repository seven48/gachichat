import hashlib
import binascii
import os

import requests
from django.db import models

from engine.serializer import to_json
from users.models import UserProfile


class RoomManager(models.Manager):
    @staticmethod
    def hash_pass(password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac(
            'sha512',
            password.encode('utf-8'),
            salt,
            100000
        )
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_pass(hashed, password):
        salt = hashed[:64]
        stored_password = hashed[64:]
        pwdhash = hashlib.pbkdf2_hmac(
            'sha512',
            password.encode('utf-8'),
            salt.encode('ascii'),
            100000
        )
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def new_room(self, **options):
        room = self.create(**options)
        user = UserProfile.objects.new_user(
            room=room
        )

        response = {}
        response['room'] = to_json(room)
        response['user'] = user
        if options.get('password'):
            response['password'] = options['room']['password']

        return response

    @staticmethod
    def get_room_name():
        data = requests.get('http://names.drycodes.com/1')
        name = data.json()[0]
        return name
