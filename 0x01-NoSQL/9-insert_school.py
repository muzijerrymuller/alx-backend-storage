#!/usr/bin/env python3
"""
Module for inserting a document into a MongoDB collection.
This script defines a function that inserts
a document into a MongoDB collection
with the provided keyword arguments.
It is designed to work with MongoDB using Python.
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert a document into a MongoDB collection.
    This function accepts keyword arguments,
    which are used as the fields of the document
    to be inserted into the specified MongoDB
    collection. After the insertion, it returns
    the unique identifier of the inserted document.
    Args:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection
    where the document will be inserted.
    **kwargs: Key-value pairs representing the fields and values of the document
    to be inserted.
    Returns:
    ObjectId: The unique identifier (_id) of the inserted document.
    Example:
    >>> from pymongo import MongoClient
    >>> client = MongoClient("mongodb://localhost:27017/")
    >>> db = client.mydatabase
    >>> collection = db.schools
    >>> school_id = insert_school
    (collection, name="Holberton", city="San Francisco")
    >>> print(school_id)
    """
    data = mongo_collection.insert_one(kwargs)
    
    return data.inserted_id
