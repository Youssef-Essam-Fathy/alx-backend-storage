#!/usr/bin/env python3
""" Update topics of a school document in MongoDB collection """


def update_topics(mongo_collection, name, topics):
    """
    Change all topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to query.
        name (str): The school name to update.
        topics (list of str): The list of topics approached in the school.
    """
    mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )

