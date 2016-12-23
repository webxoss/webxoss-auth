# encoding: utf-8

from flask import Blueprint
from controllers import CallbackController

callback = Blueprint('callback', __name__)

# ================================== #
# ============ routing  ============ #
# ================================== #
callback.add_url_rule('/weibo', methods=['GET'], view_func=CallbackController.callback_weibo)
