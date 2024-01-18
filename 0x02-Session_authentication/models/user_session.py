#!/usr/bin/env python3
"""
This module introduce a new function.
"""
from models.base import Base


class UserSession(Base):
    """
    new authentication class that inherits from
    SessionExpAuth
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initializing the class instances
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
