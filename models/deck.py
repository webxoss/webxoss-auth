# encoding: utf-8

import json
from mongoengine import Document, ObjectIdField, StringField, IntField, DictField

class Deck(Document):
    user_id = ObjectIdField(required=True, verbose_name=u'关联用户的数据库编号')
    name = StringField(required=True, verbose_name=u'卡组名称')
    content = DictField(required=True, verbose_name=u'卡组内容')

    win_count  = IntField(required=False, default=0, verbose_name=u'卡组获胜的次数')
    game_count = IntField(required=False, default=0, verbose_name=u'卡组游戏的次数')

    @staticmethod
    def check_verify_deck(deck_str):
        try:
            deck_content = json.loads(deck_str)
        except ValueError, e:
            return False

        return True

    @classmethod
    def get_name_list_by_user_id(cls, user_id):
        decks = Deck.objects(user_id=user_id)

        name_list = []
        for deck in decks:
            name_list.append(deck.name)

        return name_list

    @classmethod
    def get_decks_by_name(cls, user_id, deck_name):
        # decks = []
        # for deck_name in name_list:
        #     deck = Deck.objects(user_id=user_id, name=deck_name).first()
        #     if deck:
        #         decks.append(deck.to_JSON())
        # return decks
        deck = Deck.objects(user_id=user_id, name=deck_name).first()
        if deck:
            return deck
        else:
            return None

    @classmethod
    def upload_deck(cls, user_id, deck_name, deck_str):
        deck = Deck.objects(user_id=user_id, name=deck_name).first()

        if not deck:
            deck = Deck(name=deck_name, user_id=user_id)

        deck.content = json.loads(deck_str)
        deck.save()

        return deck

    def to_JSON(self):
        return {
            'name': self.name,
            'content': self.content
        }
