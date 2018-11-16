import pymongo
import datetime
import pytz

dt=datetime.datetime.now(tz=pytz.UTC)
dt_1=dt.astimezone(pytz.timezone('Etc/GMT+7'))


client=pymongo.MongoClient('mongodb://127.0.0.1:27018')

db=client.time_db




db.timedetails.insert_one({'name':'rafay','details': {'time_created': dt_1} })
