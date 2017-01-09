# encoding: utf-8

import json
from flask import request, jsonify
from decorator import check_user_login # from libs

from models import Deck

class DeckController(object):

    @classmethod
    @check_user_login
    def get_user_deck_list(user, cls):
        deck_name_list = Deck.get_name_list_by_user_id(str(user.id))
        return jsonify({
            'result': 0,
            'data': deck_name_list
        })

    @classmethod
    @check_user_login
    def get_user_decks(user, cls):
        deck_name = request.args.get('name', '')
        deck = Deck.get_decks_by_name(str(user.id), deck_name)
        if deck == None:
            return jsonify({
                'result': -3,
                'msg': 'Deck Not Found'
            })
        else:
            return jsonify({
                'result': 0,
                'data': deck.to_JSON()
            })

    @classmethod
    @check_user_login
    def update_user_deck(user, cls):
        deck_name = request.args.get('name', None)
        deck_content_str = request.args.get('content', '')

        if deck_name == None or not Deck.check_verify_deck(deck_content_str):
            return jsonify({
                'result': -2,
                'msg': 'Not Object'
            })

        Deck.upload_deck(str(user.id), deck_name, deck_content_str)

        return jsonify({
            'result': 0,
        })
