#!/usr/bin/env python3
"""
main
"""


import requests


def register_user(email: str, password: str) -> None:
    """register new user
    """
    response = requests.post('http://0.0.0.0:5000/users', data={
        'email': email,
        'password': password
    })
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """log-in wrong password
    """
    response = requests.post('http://0.0.0.0:5000/sessions', data={
        'email': email,
        'password': password
    })
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """log-in
    """
    pass


def profile_unlogged() -> None:
    """unlogged profile
    """
    pass


def profile_logged(session_id: str) -> None:
    """logged profile
    """
    pass


def log_out(session_id: str) -> None:
    """log out
    """
    pass


def reset_password_token(email: str) -> str:
    """reset password token
    """
    pass


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """update password
    """
    pass


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
