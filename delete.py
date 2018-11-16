import pymongo
from bson.objectid import ObjectId

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.flights
db.flightData.delete_one({'_id': ObjectId('5be210e0c8ffb760da5579a5')}) 