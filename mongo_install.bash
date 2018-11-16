MONGO DB DOCUMENTS

#create user to use mongo db
db.createUser({user:"admin", pwd:"1", roles:[{role:"root", db:"admin"}]})

=================
# DATA FORMAT
[
  {
    "departureAirport": "MUC",
    "arrivalAirport": "SFO",
    "aircraft": "Airbus A380",
    "distance": 12000,
    "intercontinental": true
  },
  {
    "departureAirport": "LHR",
    "arrivalAirport": "TXL",
    "aircraft": "Airbus A320",
    "distance": 950,
    "intercontinental": false
  }
]
#OPERATIONS

show dbs # to show currently databases
use flights #will create flights data automaticaly

#TO INSERT/CREATE
db.flightData.insertOne({name:'wajeeh',marker:'khi'})

db.flight.insertMany({your_data})
#TO READ
db.flightData.findOne({your_condition})
db.flightData.find({your_condition})
#it will update document that will lie under your_condtion and add new_field to it with new_value
db.flight.updateOne({your_condition},{$set :{new_field:'new_value'}})
#it will update all here {} means all documents of flightdata(which is a collection)
db.flightData.updateMany({your_condition},{$set :{marker:'todel'}})
#here pretty() is used to show data in desirable format
db.flightData.find({intercontinental:true}).pretty()

#here gt means greater than and lt means less then
db.flightData.find({distance : {$gt : 10000}}).pretty()
db.flightData.find({distance : {$lt : 10000}}).pretty()

======================UPDATE===========================
db.update is equal to replaceone

db.replaceOne({your_condition},{document to be replaced})

#update one will only update or add field but replace one
#willl replace entire documents with the new one provided in the
#arguments
==============PASSENGET DATA===================
#to show all the data at once
db.passenger.find().toArray()
#we can use every document and use them in fucntion
