#!/usr/bin/env python3
"""
Encrypt passwords
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """ hash a password
    """
    hashed = bcrypt.hashpw(b"{password}", bcrypt.gensalt())
    return hashed
