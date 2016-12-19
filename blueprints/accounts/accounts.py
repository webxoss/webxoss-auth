# encoding: utf-8

from flask import Blueprint
from controllers import AccountsController

accounts = Blueprint('accounts', __name__)

# ================================== #
# ============ routing  ============ #
# ================================== #
accounts.add_url_rule('/hello/<int:id>', methods=['GET'], view_func=AccountsController.hello)
