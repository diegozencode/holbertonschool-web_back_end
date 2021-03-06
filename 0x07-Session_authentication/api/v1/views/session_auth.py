#!/usr/bin/env python3
"""Module of session auth view
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """Verify credentials
    """
    email = request.form.get('email')
    passwd = request.form.get('password')
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if passwd is None:
        return jsonify({"error": "password missing"}), 400

    try:
        search = User.search({'email': email})
    except KeyError:
        return None
    if not search:
        return jsonify({"error": "no user found for this email"}), 404
    for user in search:
        if not user.is_valid_password(passwd):
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        session = auth.create_session(user.id)
        out = jsonify(user.to_json())
        out.set_cookie(getenv('SESSION_NAME'), session)
        return out


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def delete_session(user_id: str = None) -> str:
    """ DELETE session
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
