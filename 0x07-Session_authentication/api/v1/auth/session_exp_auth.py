#!/usr/bin/env python3
"""
Session auth expiration
"""


from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """session exp
    """
    def __init__(self):
        """initialize
        """
        session_d = getenv('SESSION_DURATION')
        if session_d is None or not int(session_d):
            self.session_duration = 0

        self.session_duration = int(session_d)

    def create_session(self, user_id=None):
        """create new session
        """
        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
            }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """value of the user id
        """
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        user_id = session_dictionary.get('user_id')
        if self.session_duration <= 0:
            return user_id
        if "created_at" not in session_dictionary:
            return None
        created_at = session_dictionary.get('created_at')
        if (created_at +
           timedelta(seconds=self.session_duration) < datetime.now()):
            return None
        return user_id
