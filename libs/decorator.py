# encoding: utf-8

# 检查参数中是否包括了token信息
# 并根据token信息定位到用户并且将用户信息传入函数
def check_user_login(fn):

    from flask import request, jsonify
    from models import User

    def wrapper(*args, **kwargs):
        token = request.args.get('token', '')
        user = User.get_by_token(token)
        if not user:
            return jsonify({
                'result': -1,
                'msg': 'Wrong Token'
            })
        else:
            return fn(user, *args, **kwargs) # !!!IMPORTANT!!! user 信息的传入

    return wrapper
