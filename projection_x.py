import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.movieData

data=db.movies.find({},
	{
	'_id':False,
	'name':True,
	'genres':True,
	'rating':True
	}
	)

for x in data:
	print(x)