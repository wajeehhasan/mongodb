import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')



db=client.boxoffice


raw_data=db.boxdata.find()

data=db.boxdata.find().sort([('meta.rating',-1),('meta.runtime',1)])
for x in data:
	print('\n',x,'\n')