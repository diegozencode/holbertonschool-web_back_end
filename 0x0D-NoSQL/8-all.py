#!/usr/bin/env python3
"""
List all documents
"""


from pymongo import MongoClient


def list_all(mongo_collection):
    if mongo_collection.find().count() > 0:
        return list(mongo_collection.find())
    return []
