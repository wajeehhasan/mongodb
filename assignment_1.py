import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')

db=client.hospital


#TASK 4 DELETE PATIENT WITH DISEASE FLUE
print(db.patients.delete_one({'history' : {"disease" : "headach",
	"treatment" : "on-going"}}))




#TAST3 SHOW PATIENTS LESS THAN 30 AGE
# =============================================
for x in db.patients.find({'age':{'$lt':30}}):
	print(x)
# ============================================






#TAST 2 UPDATE PATIENT NAME AGE AND HISTORY
# ======================================================
db.patients.update_one({'age':29},{'$set':
	{
	'firstName':'hax',
	'age':30,
	'history':
			{
				'disease':'alzhmers',
				'treatment':'discharged'
			}	

	}})

# ==================================================




# ===============================================
#UPDATE ANY ONE PATIENT HISTORY

db.patients.update_one({'age':{'$lt': 20}},{'$set':{
	'history':{
				'disease':'flue',
				'treatment':'not going'
				}
	}})
db.patients.update_one({'age':{'$gt': 32}},{'$set':{
	'history':{
				'disease':'headach',
				'treatment':'on-going'
				}
	}})
# ==================================================




# ==================================================
#TASK1
# INSERT PATIENTS RECORDS DONE
#DATA ADDITION DONE
db.patients.insert_one({
	'firstName':'Max',
	'lastName':'shalwar',
	'age':29,
	'history':[
				{
				'disease':'cold',
				'treatment':'on-going'
				}
	]
	})
db.patients.insert_one({
	'firstName':'wajeeh',
	'lastName':'hasan',
	'age':18,
	})
db.patients.insert_one({
	'firstName':'rafay',
	'lastName':'hasan',
	'age':18,
	})
db.patients.insert_one({
	'firstName':'zahra',
	'lastName':'hasan',
	'age':16,
	})
db.patients.insert_one({
	'firstName':'baba',
	'lastName':'hasan',
	'age':35,
	})
# ===============================================