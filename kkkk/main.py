import os,pprint,re
from datetime import datetime, date, time
import read, zipped, db
import configuration as conf

pattern = []
fields = {}
database = {}
for c in conf.config:
	p = conf.config[c].get('pattern')
	pattern.append(p)

	lineHeader = conf.config[c].get('header')
	lineDatatype = conf.config[c].get('datatype')
	lineData = conf.config[c].get('data')
	field = conf.config[c].get('field')
	fields[c] = field

files = read.getFile()
fileReads = read.reader(files,pattern,lineHeader,lineData,lineDatatype)


def convertType(fileReads):
	
	for types in fileReads:
		countDatatype = len(fileReads[types]['dataType'][0])
		countData = len(fileReads[types]['data'])
		#print types
		for index in range(0,countData):
			for x in range(0,countDatatype):
				if fileReads[types]['dataType'][0][x] == 'INTEGER':
					fileReads[types]['data'][index][x] = int(fileReads[types]['data'][index][x])

	return fileReads
confileReads = convertType(fileReads)

dicts = zipped.zipFile(confileReads)
def setTimestamp(dicts):
	timestamp = { 'timestamp' : datetime.utcnow()}
	for d in dicts:
		count = len(dicts[d])
		for c in xrange(0,count):
			dicts[d][c].update(timestamp)
	return dicts
setTimestamp(dicts)
def customize(dicts):
	record = {}
	for file in dicts:
		nameDB = 'report_'+file
		for regs in fields[file]:
			for lists in dicts[file]:
				for keys in lists.keys():
					matchs = re.match('(\w+)?'+regs+'(\w+)?', keys)
					if matchs is not None:
						key = matchs.group()
						del lists[key]

		dicts[nameDB] = dicts[file]
		del dicts[file]

	return dicts

dataToInserts = customize(dicts)

def inserts(dataToInserts):
	for tables in dicts:
		for record in dicts[tables]:
			records = {}
			records[tables] = record
			result = db.insert(records)
			print result
inserts(dataToInserts)

