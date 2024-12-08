#!/usr/bin/env python3
"""
Module for listing all documents in a MongoDB collection.
This script defines a function that retrieves and returns all the documents
from a specified MongoDB collection. It provides an easy interface to work
with data stored in MongoDB using Python.
"""
import pymongo


def list_all(mongo_collection):
    """
    Retrieve and list all documents from a specified MongoDB collection.
    Args:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection
    object from which to retrieve documents.
    Returns:
    list: A list containing all documents in the collection.
    Returns an empty list if the collection is None or empty.
    Example:
        >>> from pymongo import MongoClient
        >>> client = MongoClient("mongodb://localhost:27017/")
        >>> db = client.mydatabase
        >>> collection = db.mycollection
        >>> documents = list_all(collection)
        >>> print(documents)
    """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [post for post in documents]
