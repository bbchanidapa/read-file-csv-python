import os,pprint,re,shutil
import read,zipped,db,settime,filterfield,converttype
import configuration as conf

patterns = []
fields = {}
database = {}

for line in conf.config:
	pattern = conf.config[line].get('pattern')
	patterns.append(pattern)
	lineHeader = conf.config[line].get('header')
	lineDatatype = conf.config[line].get('datatype')
	lineData = conf.config[line].get('data')
	field = conf.config[line].get('field')
	fields[line] = field

files = read.getFile(patterns)
fileReads = read.reader(files,patterns,lineHeader,lineData,lineDatatype)
dataToFileZip = converttype.convertType(fileReads)
dicts = zipped.zipFile(dataToFileZip)
settime.setTimestamp(dicts)
filterfield.cutField(dicts,fields)

# pprint.pprint(dicts)
# print fileReads

results = []
for key in dicts:
	for record in dicts[key]:
		records = {}
		for insertFile in record:
			records[key] = record[insertFile]
			#print records,insertFile
			result = db.insert(records)
			if result != '':
				if insertFile not in results:
					results.append(insertFile)
					print insertFile
					shutil.move("C:/Users/BBB/Desktop/python/cdr/"+insertFile, "C:/Users/BBB/Desktop/python/read_already/"+insertFile)

