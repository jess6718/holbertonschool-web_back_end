#!/usr/bin/env python3
"""pyMongo"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    doc_list = []
    for item in mongo_collection.find():
        doc_list.append(item)
    return doc_list
