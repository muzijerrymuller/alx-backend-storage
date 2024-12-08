#!/usr/bin/env python3
"""
Module for updating a document in a MongoDB collection.
This script defines a function that updates the
'topics' field of documents in a MongoDB
collection where the 'name' field
matches a specified value. The function modifies all
matching documents by setting the
'topics' field to the provided value.
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update the 'topics' field of documents with
    a specific 'name' in a MongoDB collection.
    This function updates all documents in the
    specified MongoDB collection that have a 'name'
    field matching the given 'name' argument.
    It changes the 'topics' field of those documents
    to the provided 'topics' value.
    Args:
    mongo_collection (pymongo.collection.Collection):
    The MongoDB collection in which
    the documents will be updated.
    name (str): The name of the documents to be updated.
    topics (list): A list of topics to be set for the matching documents.
    Returns:
    pymongo.results.UpdateResult: The result of the update operation, containing
    information about the number of documents matched and modified.
    Example:
    >>> from pymongo import MongoClient
    >>> client = MongoClient("mongodb://localhost:27017/")
    >>> db = client.mydatabase
    >>> collection = db.schools
    >>> update_result = update_topics
    (collection, "Holberton", ["AI", "Blockchain"])
    >>> print(update_result.modified_count)
    """
    return mongo_collection.update_many(
        {
            "name": name
        },
        {
            "$set": {
                "topics": topics
            }
        })
