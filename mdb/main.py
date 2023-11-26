import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

cluster = "mongodb+srv://shafeeq:11YpZQzpzbHLSmiI@cluster0.schpx.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(cluster)

print(client.list_database_names())

db = client.test

print(db.list_collection_names())

todo = {"name" : "shafeeq" ,
        "test" : "my todo" , 
        "status" : "open"  ,
        "tags" : ["python","coding"] ,
        "date" : datetime.datetime.utcnow()
        }

todos = db.todos

#result = todos.insert_one(todo)

todo1 = [
        {"name" : "shafeeq" ,
        "test" : "my todo" , 
        "status" : "open"  ,
        "tags" : ["python","coding"] ,
        "date" : datetime.datetime.utcnow()
        } 
        ,
        {"name" : "chaps" ,
        "test" : "my todo" , 
        "status" : "open"  ,
        "tags" : ["c","coding"] ,
        "date" : datetime.datetime.utcnow()
        }
        ]

# result = todos.insert_many(todo1)

# result = todos.find({"name":"shafeeq"})
print(todos.count_documents({"tags":"c"}))

# result = todos.update_one({"tags":"c"} , {"$set" : {"surname":"chaps"}})
