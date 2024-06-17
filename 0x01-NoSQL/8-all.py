#!/usr/bin/env python3
"""No module importing"""


def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection to query.

    Returns:
        pymongo.cursor.Cursor:
        A cursor to the documents in the collection.
    """

    school = mongo_collection.find()
    return school
