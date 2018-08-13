def convertType(fileReads):
	#print 'converttype >> ',fileReads
	for typeFile in fileReads:
		lenData = len(fileReads[typeFile]['data'])
		for indexDatas in range(lenData):
			for fileName in fileReads[typeFile]['data'][indexDatas]:
				#print fileName
				datas = len(fileReads[typeFile]['data'][indexDatas][fileName])####### data for key Filename
				for indexData in range(datas):
					countData = len(fileReads[typeFile]['data'][indexDatas][fileName][indexData])
					for index in range(countData):
						data = fileReads[typeFile]['data'][indexDatas][fileName][indexData][index]
						if fileReads[typeFile]['dataType'][index] == 'INTEGER':
							fileReads[typeFile]['data'][indexDatas][fileName][indexData][index] = int(fileReads[typeFile]['data'][indexDatas][fileName][indexData][index])
							#print data,type(data)
						else:pass
				# 			print data,type(data)
				# 	print
				# print '------'


		#for index in range(lenData):
			#for x in range(lenDatatype):
				#if fileReads[typeFile]['dataType'][0][x] == 'INTEGER':
					#fileReads[typeFile]['data'][index][x] = int(fileReads[typeFile]['data'][index][x])
	return fileReads