#!/usr/bin/env python3
"""
Session in database
"""


from models.base import Base


class UserSession(Base):
    """session storing
    """
    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
