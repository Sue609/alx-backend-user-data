#!/usr/bin/env python3
"""
This module instroduces a flask app
"""
import os
from api.v1.views import app_views
from typing import Tuple
from flask import request, jsonify, make_response
from models.user import User


@app_views.route('/auth_session/login', method=['POST'], strict_slashes=True)
def login() -> Tuple[str, int]:
    """
    Handles the login route for Session authentication.
    """
    not_found_res = {"error": "no user found for this email"}
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not email:
        return jsonify({ "error": "email missing" }), 400
    if not password:
        return jsonify({ "error": "password missing" }), 404
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify(not_found_res), 404
    if len(users) <= 0:
        return jsonify(not_found_res), 404
    if users[0].is_valid_password(password):
        from api.v1.app import auth
        sessiond_id = auth.create_session(getattr(users[0], 'id'))
        res = jsonify(users[0].to_json())
        res.set_cookie(os.getenv("SESSION_NAME"), sessiond_id)
        return res
    return jsonify({"error": "wrong password"}), 401
