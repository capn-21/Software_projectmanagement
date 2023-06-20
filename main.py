from dotenv import load_dotenv,find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())


password=os.environ.get("MONGODB_PWD")
connection_string=   f"mongodb+srv://chalkeom99:{password}@pcrud.yvhau8o.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(connection_string)


dbs=client.list_database_names()

test_db=client.Test
collection=test_db.list_collection_names()


print(collection)


def insert_test_doc():
    collection=test_db.Test
    test_document={
       "name": "Omkar",
       "type":"test"
    }
    inserted_id=collection.insert_one(test_document).inserted_id
    print(inserted_id)


insert_test_doc()



newdatabase=client.newdatabase
person_collection=newdatabase.person_collection

def create_documents():
    fnames=["popo","john","doe","jane","sahil"]
    lnames=["man","connor","donner","foe","patil"]
    ages=[19,34,45,12,45]

    docs=[]
    for fname,lname,age in zip(fnames,lnames,ages):
        doc={"fname":fname,"lname":lname,"age":age}
        docs.append(doc)
        #person_collection.insert_many(docs)
    person_collection.insert_many(docs)
create_documents()



def findallpeople():
    people=person_collection.find({})

    for i in people:
        print(i)


findallpeople()
