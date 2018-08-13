from pymongo import MongoClient
from datetime import datetime, date, time
 
client = MongoClient("mongodb://192.168.190.30:27017")
database = client['case']

def insert(records):
	for namedb in records:
		db = database[namedb]
		_id = db.insert_one(records[namedb]).inserted_id
	return  _id

