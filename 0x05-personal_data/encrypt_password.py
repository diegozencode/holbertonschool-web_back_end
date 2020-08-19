#!/usr/bin/env python3
"""
Encrypt passwords
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """ hash a password
    """
    passwd = u"{password}"
    hashed = bcrypt.hashpw(passwd.encode('utf8'), bcrypt.gensalt())
    return hashed
