#!/usr/bin/env python3
"""
List all documents
"""


from pymongo import MongoClient


def list_all(mongo_collection):
    documents = mongo_collection.find()
    if documents is None:
        return []
    return documents
