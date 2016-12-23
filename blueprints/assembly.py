# encoding: utf-8

from accounts import accounts
from callback import callback
from userinfo import userinfo

def assembly(app):
    app.register_blueprint(accounts, url_prefix='/accounts')
    app.register_blueprint(callback, url_prefix='/callback')
    app.register_blueprint(userinfo, url_prefix='/userinfo')