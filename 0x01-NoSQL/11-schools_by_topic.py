#!/usr/bin/env python3
"""A function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic (str): will be the topic searched

    Return:
        List of specfic topic

    """
    documents = mongo_collection.find({"topics":topic})

    return list(documents)
