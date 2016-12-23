# encoding: utf-8

from mongoengine import *

class Config(Document):
    user_id = ObjectIdField(required=True, verbose_name=u'关联用户的数据库编号')
    content = DictField(required=False, default={}, verbose_name=u'设置内容')

    @classmethod
    def get_by_user_id(cls, user_id):
        config = Config.objects(user_id=user_id).first()
        if config:
            return config.content
        else:
            return {}

    @classmethod
    def update_config(cls, user_id, config_obj):
        config = Config.objects(user_id=user_id).first()
        if not config:
            config = Config(user_id=user_id)
        config.content = config_obj
        config.save()
        return config
