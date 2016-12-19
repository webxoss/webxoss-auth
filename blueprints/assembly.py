# encoding: utf-8

from accounts import accounts

def assembly(app):
    app.register_blueprint(accounts, url_prefix='/accounts')
