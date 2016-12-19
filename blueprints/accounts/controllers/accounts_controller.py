# encoding: utf-8

from flask import request, jsonify

class AccountsController(object):

    @classmethod
    def hello(cls, id):
        return jsonify({
            'result': 'yes',
            'msg': str(id)
        })
