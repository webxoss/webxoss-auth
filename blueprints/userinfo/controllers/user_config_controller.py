# encoding: utf-8

import json
from flask import request, jsonify
from decorator import check_user_login # from libs

from models import User, Config

class UserConfigController(object):

    @classmethod
    @check_user_login
    def get_user_config(user, cls):
        config_content = Config.get_by_user_id(str(user.id))
        result = {
            'result': 0,
            'data': config_content
        }
        return jsonify(result)

    @classmethod
    @check_user_login
    def update_user_config(user, cls):
        config_str = request.args.get('config', '')

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
