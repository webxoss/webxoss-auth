# encoding: utf-8

from flask import request, jsonify, redirect, render_template
from config_loader import config

class AccountsController(object):

    @classmethod
    def login(cls):
        state = request.args.get('state', "")
    	return render_template('login.html', state=state)

    @classmethod
    def login_weibo(cls):
        state = request.args.get('state', "")
        weibo_config = config.get('oauth')['weibo']
    	login_url = "%s?client_id=%s&response_type=code&state=%s&redirect_uri=%s" % (
    		weibo_config['login_url'], 
    		weibo_config['app_key'], 
    		state, 
    		weibo_config['redirect_url']
    	)
    	return redirect(login_url, code=301)