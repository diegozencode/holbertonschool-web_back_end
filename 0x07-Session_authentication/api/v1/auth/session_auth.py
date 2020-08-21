#!/usr/bin/env python3
"""
Empty session
"""


from api.v1.auth.auth import Auth
from models.user import User
import uuid
from typing import TypeVar


class SessionAuth(Auth):
    """new authentication mechanism
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create new session
        """
        if user_id is None:
            return None
        if not type(user_id) == str:
            return None
        self.id = str(uuid.uuid4())
        self.user_id_by_session_id[self.id] = user_id
        return self.id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """value of the user id
        """
        if session_id is None:
            return None
        if not type(session_id) == str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('user'):
        """instace based on a cookie value
        """
        if request is None:
            return None
        session_id = self.session_cookie(request)
        user = self.user_id_for_session_id(session_id)
        return User.get(user)

    def destroy_session(self, request=None):
        """deletes the user session
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user = self.user_id_for_session_id(session_id)
        if not user:
            return False
        self.user_id_by_session_id.pop(session_id)
        return True
