import pymongo


client=pymongo.MongoClient('mongodb://127.0.0.1:27018')

db=client.boxoffice
#1
#import data

#2 movies with 9.2 rating and runtime <100
#with python
data=db.boxdata.find({})
for x in data:
	if x['meta']['rating']>9.2 and x['meta']['runtime']<100:
		print(x)

#with mongodb shell
data=db.boxdata.find(
	{'$and' :[ 
			{
			'meta.rating': 
							{'$gt':9.3}
			},
			{
			'meta.runtime' : 
							{'$lt':100}
			}

	]}
# 	)

#3 genre drama or action
#python
for x in data:
	if 'drama' in x['genre'] or 'action' in x['genre']:
		print(x)
# #mongodb shell

db.boxdata.find(
	{'$or' : [
			{'genre' : 'drama'},
			{'genre' : 'action'}

	]
	}
	)
#4 visitor exceeded visitor expected
# mongoshell
db.boxdata.find({$expr : {$gt : ['$visitors','$expectedVisitors'] }})


#with python
for x in data:
	if x['visitors']>x['expectedVisitors']:
		print(x)














