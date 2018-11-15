import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27018')

db=client.companies

"""we can enable journaling by this in pymong"""
# m = pymongo.MongoClient()
# m.write_concern = {'w': 1}
# m.write_concern['j'] = True


#1
db.comp.insert_one(
	{
	'name':'company A',
	'type':'trading'
	}

	)
db.comp.insert_many([
	{
	'_id':'myb',
	'name':'company B',
	'type':'seller'
	},
	{
	'name':'company C',
	'type':'wholesd'}
	])

#2
try:
	db.comp.insert_many([
		{
		'_id':'myb',
		'name':'company B',
		'type':'seller'
		},
		{
		'name':'company D',
		'type':'presales'

		}
		],
		ordered=False
		)
except:
	print('duplication occured')

db.comp.insert_one({'name':'company E'},
	{
	'writeConcern' : 
					{
					'w':1,'j': True
					}
	}
	)
db.comp.insert_many([{'name':'company F'},{'name':'company G'},
	{
	'writeConcern' : 
					{
					'w':1,'j':True
					}
	}
	])
db.comp.insert_one({'name':'company H'},
	{
	'writeConcern' : 
					{
					'w':1,'j':False
					}
	}
	)






















