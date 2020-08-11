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
        return False

    def authorization_header(self, request=None) -> str:
        """Nothing so far
        """
        return None

    def current_user(self, request=None) -> TypeVar('user'):
        """Nothign so far
        """
        return None
