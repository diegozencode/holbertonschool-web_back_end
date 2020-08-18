#!/usr/bin/env python3
"""
Regex-ing
"""


from typing import List
import logging
import re
import os
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values
        """
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


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


def get_logger() -> logging.Logger:
    """parameterize the formatter
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formater = RedactingFormatter(PII_FIELDS)

    handler.setFormatter(formater)
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connector to the database
    """

    HOST = os.getenv('PERSONAL_DATA_DB_HOST')
    DATABASE = os.getenv('PERSONAL_DATA_DB_NAME')
    USER = os.getenv('PERSONAL_DATA_DB_USERNAME')
    PASSWORD = os.getenv('PERSONAL_DATA_DB_PASSWORD')

    conn = mysql.connector.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )

    return conn
