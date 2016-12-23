# encoding: utf-8

from flask import Blueprint
from controllers import AccountsController

accounts = Blueprint('accounts', __name__, template_folder='templates')

# ================================== #
# ============ routing  ============ #
# ================================== #
accounts.add_url_rule('/login', methods=['GET'], view_func=AccountsController.login)
accounts.add_url_rule('/login/weibo', methods=['GET'], view_func=AccountsController.login_weibo)
