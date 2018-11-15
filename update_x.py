import pymongo
# from bson.objectid import ObjectId

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.userdata

for x in db.users.update_one({"_id" : ObjectId("5bec5936790e03c28f6374fe")},{'age':30}):
	print(x)

