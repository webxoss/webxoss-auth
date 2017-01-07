# encoding: utf-8

from mongoengine import Document, ObjectIdField, StringField, IntField

class Deck(Document):
    user_id = ObjectIdField(required=True, verbose_name=u'关联用户的数据库编号')
    name = StringField(required=True, verbose_name=u'卡组名称')
    main_deck = StringField(required=True, verbose_name=u'主要卡组内容')
    lrig_deck = StringField(required=True, verbose_name=u'分身卡组内容')

    win_count  = IntField(required=False, default=0, verbose_name=u'卡组获胜的次数')
    game_count = IntField(required=False, default=0, verbose_name=u'卡组游戏的次数')

    @staticmethod
    def check_verify_deck(deck_str):
        try:
            card_id_list = deck_str.split(",")
            for card_id_str in card_id_list:
                card_id = int(card_id_str)
                if not card_id > 0:
                    return False
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
    def get_decks_by_name(cls, user_id, name_list):
        decks = []
        for deck_name in name_list:
            deck = Deck.objects(user_id=user_id, name=deck_name).first()
            if deck:
                decks.append(deck.to_JSON())
        return decks

    @classmethod
    def upload_deck(cls, user_id, deck_name, main_deck, lrigh_deck):
        deck = Deck.objects(user_id=user_id, name=deck_name).first()

        if not deck:
            deck = Deck(name=deck_name, user_id=user_id)

        deck.main_deck = main_deck
        deck.lrig_deck = lrig_deck
        deck.save()

        return deck

    def to_JSON(self):
        return {
            'main_deck': self.main_deck,
            'lrig_deck': self.lrig_deck
        }
