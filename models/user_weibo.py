# encoding: utf-8

from mongoengine import Document, StringField, ObjectIdField

from user import User

class UserWeibo(Document):
    uid = StringField(required=True, verbose_name=u'新浪微博中的uid')
    user_id = ObjectIdField(required=True, verbose_name=u'关联用户的数据库编号')

    @classmethod
    def login_by_uid(cls, uid):
        user_linker = UserWeibo.objects(uid=uid).first()
        if user_linker:
            user = User.get_by_id(str(user_linker.user_id))
        else:
            user = User.create_user()
            user_linker = UserWeibo(
                uid=uid,
                user_id=user.id
            )
            user_linker.save()

        user.refresh_token()
        return user
