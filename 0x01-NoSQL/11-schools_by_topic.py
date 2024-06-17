#!/usr/bin/env python3
""" Module to find schools by topic """


def schools_by_topic(mongo_collection, topic):
    """
    Find and return schools that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection to query.
        topic (str): The topic to search for in the schools' topics list.

    Returns:
        pymongo.cursor.Cursor: A cursor to the documents in the collection that
        match the topic.
    """
    return mongo_collection.find({'topics': topic})
