import re,csv,os

def getFile(patterns):
	read_file = os.listdir('../cdr')#('../cdr')
	files = []
	for count in range(5):
		fileName = read_file[count]
		for pattern in patterns:
			reg = fileName.startswith(pattern)
			if reg == True:
				files.append(fileName)
	return files

def reader(files,patterns,lineHeader,lineData,lineDatatype):
	lists = {}
	data = {}
	for file in files:
		# print '----'
		# print 'file : ',file
		# print
		for pattern in patterns:
			#print 'pattern : ',p
			#print
			reg = file.startswith(pattern)
			if reg == True:
				if pattern not in lists:
					#print 'not found : ',p
					#print 'create new'
					#print
					lists[pattern]	= {
						'header' : [],
						'dataType' : [],
						'data' : []
					}
				with open('../cdr/'+file, 'rb') as csvfile:
				#with open(file, 'rb') as csvfile:
					# print 'open file :',file
					# print

					read = csv.reader(csvfile)
					count = 0
					for line in read:
						if count == lineHeader:
							if line not in lists[pattern]['header']:
								#print 'add header :',r
								lists[pattern]['header'] = line
						elif count == lineDatatype:
							if line not in lists[pattern]['dataType']:
								lists[pattern]['dataType'] = line
						elif count >= lineData:
							fileNames = {}
							if file not in fileNames:
								#print file,'add To Lists : if >>',line
								fileNames[file] = []
								fileNames[file].append(line)
							elif file in fileNames:
								#print file,'add To Lists : else >>',line
								fileNames[file].append(line)
							lists[pattern]['data'].append(fileNames)

						count+=1
					#print '------------End------------'

	return lists
