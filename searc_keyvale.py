import pymongo
#finding a document where distance >10000

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.flights

for x in db.flightData.find({'distance':{'$gt':10000}}):
	print(x)

