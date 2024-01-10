#!/usr/bin/env python3
"""pyMongo"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school with a topic"""
    my_query = {"topics": topic}
    my_list = mongo_collection.find(my_query)
    return my_list
