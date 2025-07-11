#!/usr/bin/env python3
def list_all(mongo_collection):
    '''Task 8'''
    return list(mongo_collection.find())
