import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')



db=client.teams
#1 upsert 2 documents
db.sports.update_one(
	{
	'name':'team b'
	},
	
	{
	'$set' : {'title':'khi','requiresTeam': False}
	
	},
	upsert= True
	)
db.sports.update_one(
	{
	'name':'team a'
	},
	
	{
	'$set' : {'title':'lhr','requiresTeam': True}
	
	},
	upsert= True
	)


#2 update documents which do require a team and add field team with a number of required players


db.sports.update_many(
	{
	'requiresTeam': True
	},
	{'$set':
			{
			'team_number':10
			}
	}
	)	

#3 increment team_number by 10

db.sports.update_many(
	{
	'requiresTeam':True
	},
	{'$inc':
			{'team_number':10}

	}
	)