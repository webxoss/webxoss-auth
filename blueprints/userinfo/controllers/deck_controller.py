# encoding: utf-8

import json
from flask import request, jsonify

from models import Deck

class DeckController(object):

    @classmethod
    @check_user_login
    def get_user_deck_list(user, cls):
        pass

    @classmethod
    @check_user_login
    def get_user_decks(user, cls):
        pass

    @classmethod
    @check_user_login
    def update_user_deck(user, cls):
        pass
