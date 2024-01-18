#!/usr/bin/env python3
"""
This module introduces a new class.
"""
from .auth import Auth
import uuid


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
