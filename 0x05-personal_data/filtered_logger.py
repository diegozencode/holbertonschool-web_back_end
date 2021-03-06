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


def main() -> None:
    """read and filter data
    """
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM users;"
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        message = (
            f"name={row[0]}; "
            f"email={row[1]}; "
            f"phone={row[2]}; "
            f"ssn={row[3]}; "
            f"password={row[4]}; "
            f"ip={row[5]}; "
            f"last_login={row[6]}; "
            f"user_agent={row[7]}"
        )
        log_record = logging.LogRecord(
            "user_data", logging.INFO, None, None, message, None, None
            )
        formatter = RedactingFormatter(PII_FIELDS)
        print(formatter.format(log_record))
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
