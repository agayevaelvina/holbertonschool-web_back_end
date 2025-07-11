#!/usr/bin/env python3
'''x'''
def schools_by_topic(mongo_collection, topic):
    """x"""
    return list(mongo_collection.find({"topics": topic}))
