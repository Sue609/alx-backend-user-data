#!/usr/bin/env python3
"""
This module introduces a new class.
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """
    Class that inherits from SessionAuth with expiration.
    """
    def __init__(self) -> None:
        """
        Initializing the new class instances
        """
        super().__init__()
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION", 0))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None) -> str:
        """
        Creating a session id that will call this methos.
        Return: The session ID created.
        """
        session_id = super().create_session(user_id)
        if type(session_id) != str:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'session_id': datetime.now()
        }

        return session_id

    def user_id_for_session_id(self, session_id: str = None):
        """
        Overloaded method to get user_id for a given session_id.
        """
        if session_id in self.user_id_by_session_id:
            new_session = self.user_id_by_session_id[session_id]
            if self.session_duration <= 0:
                return new_session['user_id']
            if 'created_at' not in new_session:
                return None
            current_time = datetime.now()
            time_span = timedelta(seconds=self.session_duration)
            expiry_time = new_session['created_at'] + time_span
            if expiry_time < current_time:
                return None
            return new_session['user_id']
