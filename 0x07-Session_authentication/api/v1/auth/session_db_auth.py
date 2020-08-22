#!/usr/bin/env python3
"""
session authentication db
"""


from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """session db auth
    """
    def create_session(self, user_id=None):
        """create a session
        """
        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session = UserSession(user_id, session_id)
        session.save()
        return session

    def user_id_for_session_id(self, session_id=None):
        """user id for session id
        """
        if session_id is None:
            return None
        return self.user_id_by_session_id.get(session_id)

    def destroy_session(self, request=None):
        """destroy the user session
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
