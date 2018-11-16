import pymongo
#updating many fields with 1 command
client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.flights
status={'$set' :{'hobbies':['computer','reading','sports']}}
filter_1={'name':{'$in' :['Armin Glutch','Albert Twostone']}}
db.passenger.update_many(filter_1,status)