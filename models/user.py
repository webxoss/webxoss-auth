# encoding: utf-8

import random
from datetime import datetime, timedelta
from mongoengine import *

class User(Document):
    token = StringField(required=True, verbose_name=u'认证的token')
    access_time = DateTimeField(required=True, verbose_name=u'token的有效截止时间')

    _REFRESH_TIME = 3600 * 4

    @classmethod
    def random_token(self):
        return "%032x" % random.getrandbits(128)

    def refresh_token(self):
        token = User.random_token()
        while User.objects(token=token).count() > 0:
            token = User.random_token()

        self.token = token
        self.access_time = datetime.now() + timedelta(seconds = User._REFRESH_TIME)
        self.save()

    @classmethod
    def create_user(cls):
        user = User(
            token=User.random_token(),
            access_time=datetime.now()
        )
        user.save()
        return user

    @classmethod
    def get_by_id(cls, user_id):
        user = User.objects(id=user_id).first()
        return user
