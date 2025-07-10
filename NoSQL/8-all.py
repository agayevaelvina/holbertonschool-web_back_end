#!/usr/bin/env python3
from pymongo import MongoClient
def list_all(mongo_collection):
    documents= list(mongo_collection.find())
client =MongoClient("mongodb://localhost:27017/")
db = client["database1"]
collection = db["school"]  
documents = list_all(collection)
print(documents)

