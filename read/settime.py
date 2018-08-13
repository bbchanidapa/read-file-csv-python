from datetime import datetime, date, time
def setTimestamp(dicts):
	timestamp = { 'timestamp' : datetime.utcnow()}
	for key in dicts:
		for record in dicts[key]:
			for file in record:
				record[file].update(timestamp)
			# 	count = len(record[file])
				# for c in range(count):
				# 	print record[file][c]
					#record[file][c].update(timestamp)
		#print dicts
	return dicts