#!/usr/bin/env python3
"""
Regex-ing
"""


from typing import List
import logging
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Filter fields
    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing separation all fields in the log line
    Return:
        log message obfuscated
    """
    for field in fields:
        message = re.sub(r'{}=(.+?){}'.format(field, separator),
                         r'{}={}{}'.format(field, redaction, separator),
                         message)
    return message
