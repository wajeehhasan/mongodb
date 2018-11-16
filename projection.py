import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


#to get only required data

db=client.test_flights
db.flightData.insert_many(lit_flightdata)
db.passenger.insert_many(lit_passenger)


# for projection

for elem in db.passenger.find({},{'name':1,'_id':0}):
	print(elem)