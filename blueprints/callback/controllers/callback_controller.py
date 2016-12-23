# encoding: utf-8

import requests
import json
from flask import request, jsonify, redirect
from config_loader import config

from models import User, UserWeibo

class CallbackController(object):

    # 所有Callback方法根据内容获取到user信息，然后返回到webxoss页面

    @staticmethod
    def redirect_linker(token, access_time, state):
        redirect_url = "http://webxoss.com/?token=%s&access_time=%s&state=%s" % (token, access_time, state)
        return redirect(redirect_url, code=301)

    @classmethod
    def callback_weibo(cls):
        code = request.args.get('code', None)
        state = request.args.get('state', None) # 用于给webxoss验证用参数
        if code == None:
            return jsonify({
                'result': -1,
                'msg': 'Code Error'
            })

        weibo_config = config.get('oauth')['weibo']
        
        # 根据code获取uid信息
        get_params = {
            'client_id': weibo_config['app_key'],
            'client_secret': weibo_config['app_secret'],
            'redirect_uri': weibo_config['redirect_url'],
            'grant_type': 'authorization_code',
            'code': code,
        }
        res = requests.post(weibo_config['access_token_request_url'], params=get_params)
        res_obj = json.loads(res.text)
        weibo_uid = res_obj['uid']

        # 根据uid在数据库中查询用户
        user = UserWeibo.login_by_uid(weibo_uid)

        # 回传一个Redirect指令
        return CallbackController.redirect_linker(user.token, User._REFRESH_TIME, state)
