#!/usr/bin/env python3
"""
This module introduces a new class.
"""
from .auth import Auth
import uuid
from models.user import User
from flask import request


class SessionAuth(Auth):
    """
    A class that inherits from the Auth class.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Class instance method that creates a session id
        for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Intance method that returns a User ID based on the
        session_id
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        """
        Instance method that returns a user instance based on cookie
        value
        """
        user_id = self.user_id_by_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Method that delets the user session / logout
        """
        if request is None:
            return False
        session_cookie_value = self.session_cookie(request)
        if not session_cookie_value:
            return False
        user_id = self.user_id_for_session_id(session_cookie_value)
        if not user_id:
            return False
        if session_cookie_value in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_cookie_value]
        return True
