# encoding: utf-8

from flask import Blueprint
from controllers import UserinfoController

userinfo = Blueprint('userinfo', __name__)

# ================================== #
# ============ routing  ============ #
# ================================== #
userinfo.add_url_rule('/configs/v1', methods=['GET'], view_func=UserinfoController.get_user_config)
userinfo.add_url_rule('/configs/v1', methods=['POST'], view_func=UserinfoController.update_user_config)

# userinfo.add_url_rule('/decks/list/v1', methods=['GET'], view_func=UserinfoController.get_user_deck_list)
# userinfo.add_url_rule('/decks/v1', methods=['GET'], view_func=UserinfoController.get_user_decks)
# userinfo.add_url_rule('/decks/v1', methods=['POST'], view_func=UserinfoController.update_user_deck)
