#!/usr/bin/env python3
"""
Basic Authentication
"""

import base64
import binascii
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """base64
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

    def decode_base64_authorization_header(self,
                                           base_authorization_header: str
                                           ) -> str:
        """decode base64
        """
        if base_authorization_header is None:
            return None
        if not type(base_authorization_header) == str:
            return None
        try:
            base64_bytes = base_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            return message_bytes.decode('utf-8')
        except binascii.Error:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """user credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not type(decoded_base64_authorization_header) == str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        result = decoded_base64_authorization_header.find(":")
        header_one = decoded_base64_authorization_header[:result]
        header_two = decoded_base64_authorization_header[result + 1:]
        return header_one, header_two
