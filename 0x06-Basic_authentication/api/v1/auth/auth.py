#!/usr/bin/env python3
"""
API Authentication
"""


from flask import request
from typing import List, TypeVar


class Auth():
    """Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Nothing so far
        """
        if path is None:
            return True
        if excluded_paths is None:
            return True
        my_list = [x[:-1] for x in excluded_paths if x[-1] == '/']
        if path in excluded_paths or path in my_list:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Nothing so far
        """
        return None

    def current_user(self, request=None) -> TypeVar('user'):
        """Nothign so far
        """
        return None
