#!/usr/bin/env python3
"""A function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score

    Args:
        mongo_collection: pymongo collection object

    Return:
        Top scores of students in the collection
    """
    top_score = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_score
