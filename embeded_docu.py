#create embeded docu updating
import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.flights
status={'$set' :{ 'status':{'description':'holatime','plane':{'size':'mumbo','others':{'model':'7479boeing'}}}}}
db.flightData.update_many({},status)

for x in db.flightData.find():
	print(x,'\n')