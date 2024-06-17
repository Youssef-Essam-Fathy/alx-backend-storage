#!/usr/bin/env python3
""" Insert a new school document into a MongoDB collection """


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection to insert into.
        **kwargs: Key-value pairs
        to be inserted as the document.

    Returns:
        ObjectId: The ID of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result
