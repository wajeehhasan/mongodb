import pymongo


client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.flights
#accessing data structures

for x in db.flightData.find({},{'status':1,'_id':0}):
	print(x['status']['plane']['others']['model'])

for x in db.flightData.find({'distance':{'$gt': 10000}},{'status':1,'_id':0}):
	print(x['status']['plane']['others']['model'])

