#!/usr/bin/env python3
"""
Basic Authentication
"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """base 64
        """
        header = "Basic "
        if authorization_header is None:
            return None
        if not type(authorization_header) == str:
            return None
        if len(authorization_header) < 6:
            return None
        if authorization_header.startswith(header):
            return authorization_header[6:]
        else:
            return None
