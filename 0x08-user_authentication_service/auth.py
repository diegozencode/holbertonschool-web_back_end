#!/usr/bin/env python3
"""
Hash password
"""


import bcrypt


def _hash_password(password: str) -> str:
    """hash a password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
