#!/usr/bin/env python3
"""A function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a mondbd collection

    Args:
        kwargs: Key-value pairs representing the fields and values of the document.
        mongo_collection: The collection to insert the document into.

    Returns:
        The new _id of the inserted document.
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
