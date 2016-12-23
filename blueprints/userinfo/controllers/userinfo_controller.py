# encoding: utf-8

import json
from flask import request, jsonify

from models import User, Config

class UserinfoController(object):

    @classmethod
    def get_user_config(cls):
        token = request.args.get('token', '')
        user = User.get_by_token(token)
        if not user:
            return jsonify({
                'result': -1,
                'msg': 'Wrong Token'
            })

        config_content = Config.get_by_user_id(str(user.id))
        result = {
            'result': 0,
            'data': config_content
        }
        return jsonify(result)

    @classmethod
    def update_user_config(cls):
        token = request.args.get('token', '')
        config_str = request.args.get('config', '')
        user = User.get_by_token(token)
        if not user:
            return jsonify({
                'result': -1,
                'msg': 'Wrong Token'
            })

        try:
            config_object = json.loads(config_str)
        except ValueError, e:
            return jsonify({
                'result': -2,
                'msg': 'Config is not a json object'
            })

        Config.update_config(str(user.id), config_object)
        result = {
            'result': 0
        }
        return jsonify(result)

    @classmethod
    def get_user_deck_list(cls):
        pass

    @classmethod
    def get_user_decks(cls):
        pass

    @classmethod
    def update_user_deck(cls):
        pass
