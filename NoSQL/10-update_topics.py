#!/usr/bin/env python3
"""pyMongo"""


def update_topics(mongo_collection, name, topics):
    """Update all topics of a school document based on the name"""
    my_query = {"name": name}
    new_topics = {"$set": {"topics": topics}}
    mongo_collection.update_many(my_query, new_topics)
