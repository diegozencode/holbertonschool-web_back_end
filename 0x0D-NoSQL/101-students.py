#!/usr/bin/env python3
"""
Top students
"""


from pymongo import MongoClient


def top_students(mongo_collection):
    """all students sorted by average score
    """
    query = mongo_collection.aggregate([
        {'$project': {'name': '$name',
                      'averageScore': {'$avg': '$topics.score'}}},
        {'$sort': {'averageScore': -1}}
    ])
    return query
