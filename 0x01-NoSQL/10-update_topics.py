#!/usr/bin/env python3
"""A function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics based on the name

    Args:
        mongo_collection: pymongo collection object
        name (str): the school name to update
        topics (list of strs): the list of topics approached in the school

    Returns:
        Nothing

    """
    new_value = {"name": name}
    other_value = {"$set": {"topics" :topics}}

    mongo_collection.update_many(new_value, other_value)
