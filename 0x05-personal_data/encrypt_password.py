#!/usr/bin/env python3
"""
Encrypt passwords
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """ hash a password
    """
    passwd = b"{password}"
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """check valid password
    """
    return bcrypt.checkpw(b"{password}", hashed_password)
