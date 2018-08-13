from pymongo import MongoClient
from datetime import datetime, date, time
 
client = MongoClient("mongodb://192.168.190.30:27017")
database = client['case']

def insert(records):

	for namedb in records:
		db = database[namedb]
		#print namedb
		#print 'Insert ',namedb,' : ',records[namedb]
		_id = db.insert_one(records[namedb]).inserted_id
		# print db.find_one({ "_id" : _id })
		# print
	return  _id

