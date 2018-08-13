import os,re
def cutField(dicts,fields):
	for keyDict in dicts:
		nameDB = 'report_'+keyDict
		#print '--------File',keyDict,'---------'
		for record in dicts[keyDict]:
			for file in record:
				for reg in fields[keyDict]:
					for key in record[file].keys():
						matchs = re.match('(\w+)?'+reg+'(\w+)?', key)
						if matchs is not None:
							result = matchs.group()
							del record[file][result]


		dicts[nameDB] = dicts[keyDict]
		del dicts[keyDict]

	return dicts
