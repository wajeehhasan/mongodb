import pymongo


client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.flights

db.flightData.replace_one({'model':'hoing420'},{})
#this will replace data with model with {} means empty 1