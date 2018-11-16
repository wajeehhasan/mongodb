import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


db=client.authors


for x in db.book.aggregate(
[
	{'$lookup' : {'from':'author','localField':'authors','foreignField':'_id','as':'creators'}},
	{'$match' : {'name':'A bad book'}}
]):
	print(x)










# db.book.insertOne({name:'a good book',authors:[{'_id'='"5be59e0b255e9d8091217ef8"'},{'_id':'"5be59e19255e9d8091217ef9"'}]})



# db.book.aggregate([{$lookup : {from:'author',localField:'authors',foreignField:'id'}}])
