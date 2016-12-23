# encoding: utf-8

from accounts import accounts
from callback import callback

def assembly(app):
    app.register_blueprint(accounts, url_prefix='/accounts')
    app.register_blueprint(callback, url_prefix='/callback')
