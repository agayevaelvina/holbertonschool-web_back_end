#!/usr/bin/env python3
"x"
def update_topics(mongo_collection, name, topics):
    '''Task 10'''
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
