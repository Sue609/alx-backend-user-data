#!/usr/bin/env python3
"""
This module introduces API authentication
"""
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """
    The authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        A NEW FUNCTION TO CHECK IF THE AUTHENTICATION PATH IS REQUIRED.
        It returns False - path and excluded_paths
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns None - request that will be the Flask request objects
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None - request will be the Flask request object
        """
        return None
