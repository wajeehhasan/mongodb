import pymongo
#removing single field from documents

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.flights


db.flightData.update({"distance" : 12000},{'$unset': {'model':1}});

db.flightData.update({"distance" : 12000},{'$unset': {'intercontinental':1}});