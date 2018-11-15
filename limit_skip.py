import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.movieData


data=db.movies.find({'schedule.time':'21:00'}).limit(2).skip(1)
new_list=[]
for x in data:
	print('\n',x,'\n')
	new_list.append(x)

print(len(new_list))