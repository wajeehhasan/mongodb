import pymongo


client=pymongo.MongoClient('mongodb://127.0.0.1:27018')


client.drop_database('test_flights')

client['new_db1'].drop_collection('my_col1')
# flights       0.000GB
# hospital      0.000GB
# local         0.000GB
# test_flights 

# db=client.new_db1
# db.my_col1.insert_one({'33':'y'})
# db.my_col556.insert_one({'33':'y'})
# db2=client.new_db2
# db2.my_col1.insert_one({'sds':'s'})