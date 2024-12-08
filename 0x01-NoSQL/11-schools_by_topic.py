#!/usr/bin/env python3
"""
select by spacific value
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    select by specific value
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
