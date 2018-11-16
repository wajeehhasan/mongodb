import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.persondata


data=db.persons.aggregate([
		{'$match' : {'dob.age': {'$gt':50}}},
		{
		'$group': 
			{
			'_id' : {'gender':'$gender'},
			'Person/Gender': {'$sum':1},
			'avgAge' : {'$avg' : '$dob.age'}
			}
		},
		{'$sort': {'Person/Gender':-1}}
	])

for x in data:
	print(x)
			# 'avgAGE/Gender':{'$avg' : '$dob.age'}}},