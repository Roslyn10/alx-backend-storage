#!/usr/bin/env python3
"""A function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    List all the documents in the specified mongo collection

    Args:
        mongo_collection: A pymongo collection object

    Returns:
        A list of documents in the collection
    """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return [document for document in documents]
