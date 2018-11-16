import pymongo
from bson.objectid import ObjectId

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.flights

	


# db.flightData.update_many({'distance':12000.0},{'$set':{'status': {'others':{'model':'hoing898'}}}})


db.flightData.update_many({"_id" : "5be210e0c8ffb760da5579a5"},{'$set':


{
	"_id" : "5be210e0c8ffb760da5579a5",
	"departureAirport" : "MUC",
	"arrivalAirport" : "SFO",
	"aircraft" : "Airbus A380",
	"distance" : 12000,
	"intercontinental" : 'true',
	"status" : {
		"others" : {
			"model" : "hoing898"
		}
	}
}}
)
