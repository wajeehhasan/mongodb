import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.userdata

data=db.users.find({'hobbies':
	{'$elemMatch':
					{
					'title':'Sports', 'frequency': 
													{'$gte' : 3}
					}
	
	}
	})

for x in data:
	print(x)