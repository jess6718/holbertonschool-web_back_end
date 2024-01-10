#!/usr/bin/env python3
"""Nginx logs"""
from pymongo import MongoClient


def nginx_logs(mongo_collection):
    """Some stats about Nginx logs stored in MongoDB"""
    total_doc = mongo_collection.count_documents({})
    print(f"{total_doc} logs")

    print(f"Methods:")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    tab = '\t'
    for m in method:
        total_m = mongo_collection.count_documents({"method": m})
        print(f"{tab}method {m}: {total_m}")

    total_status = mongo_collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{total_status} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    nginx_logs(nginx_collection)
