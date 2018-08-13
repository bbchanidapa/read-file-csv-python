def setTimestamp(dicts):
	timestamp = { 'timestamp' : datetime.utcnow()}
	for d in dicts:
		count = len(dicts[d])
		for c in xrange(0,count):
			dicts[d][c].update(timestamp)
	return dicts