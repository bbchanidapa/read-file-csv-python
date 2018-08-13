def zipFile(dataToFileZip):
	dicts = {}

	for filename in dataToFileZip:
		headers = dataToFileZip[filename]['header']
		datas = dataToFileZip[filename]['data']
		lists = []
		for data in datas:
			for key in data:
				for listData in data[key]:
					if listData not in lists:
						zipped = {}
						zipped[key] = dict(zip(headers,listData))
						lists.append(zipped)

		dicts[filename] = lists

	return dicts

