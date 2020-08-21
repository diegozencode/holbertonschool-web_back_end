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
    if User.is_valid_password is None:
        return jsonify({"error": "wrong password"}), 401
    for user in search:
        from api.v1.app import auth
        session = auth.create_session(user.id)
        out = jsonify(user.to_json())
        out.set_cookie(getenv('SESSION_NAME'), session)
        return out
