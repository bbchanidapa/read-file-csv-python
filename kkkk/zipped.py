def zipFile(confileReads):
	dicts = {}
	for filename in confileReads:
		headers = confileReads[filename]['header']
		datas = confileReads[filename]['data']
		for header in headers:
			lists = []
			for data in datas:
				if data not in lists:
					zipped = {}
					zipped = dict(zip(header,data))
					lists.append(zipped)
		dicts[filename] = lists

	return dicts

				# x.update({3:4})


