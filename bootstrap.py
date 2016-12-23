# coding: utf-8

import sys
import os
from mongoengine import connect

class Bootstrap(object):

    @classmethod
    def bootstrap(cls):
        cls.__using_utf8()
        cls.__include_path()
        cls.__init_config_loader()
        cls.__init_mongoengine()
        app = cls.__create_app()
        cls.__routing(app)
        return app

    @classmethod
    def __using_utf8(cls):
        reload(sys)
        sys.setdefaultencoding('utf8')

    @classmethod
    def __include_path(cls):
        """
        include project path
        """
        import os
        path = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        sys.path += [path + x for x in [
            '/',
            '/blueprints',
            '/libs',
        ]]

    @classmethod
    def __init_config_loader(cls):
        """
        初始化config loader
        蒋/config下的yaml文件绑定到config上
        """
        from config_loader import config
        config.setup('configs/', 'prod')

    @classmethod
    def __init_mongoengine(cls):
        connect('webauth', host='127.0.0.1', port=27017)

    @classmethod
    def __create_app(cls):
        """
        create flask app
        """
        from flask import Flask
        app = Flask(__name__)
        return app

    @classmethod
    def __routing(cls, app):
        """
        routing
        """
        from blueprints import assembly
        assembly(app)
