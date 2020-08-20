#!/usr/bin/env python3
"""
Empty session
"""


from api.v1.auth.auth import Auth
import uuid


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
