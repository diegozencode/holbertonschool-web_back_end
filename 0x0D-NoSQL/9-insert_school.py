#!/usr/bin/env python3
"""
insert a document
"""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    # for key, value in kwargs.items():
    _id = mongo_collection.insert(kwargs)
    return _id
