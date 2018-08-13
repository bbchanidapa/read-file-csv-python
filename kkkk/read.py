import re,csv,os

def getFile():
	read_file = os.listdir('.')
	fileAll = []
	files = []
	for r in read_file:
		fileAll.append(r)
	for x in xrange(0,5):
		f = fileAll[x]
		files.append(f)
	return files

def reader(files,pattern,lineHeader,lineData,lineDatatype):
	lists = {}
	data = {}
	for f in files:
		#print '----'
		#print 'file : ',f
		#print 
		for p in pattern:
			#print 'pattern : ',p
			#print
			reg = f.startswith(p)			
			if reg == True:	
				if p not in lists:
					#print 'not found : ',p
					#print 'create new'
					#print 			
					lists[p]	= {
						'header' : [],
						'dataType' : [],
						'data' : []
					}								
				with open(f, 'rb') as csvfile:
					#print 'open file :',f
					#print
					read = csv.reader(csvfile)
					c = 0
					for line in read:
						if c == lineHeader:
							if line not in lists[p]['header']:
								#print 'add header :',r
								lists[p]['header'].append(line)
							else:pass
						elif c == lineDatatype:
							if line not in lists[p]['dataType']:
								lists[p]['dataType'].append(line)
						elif c >= lineData:
							#print 'add data :',r
							lists[p]['data'].append(line)
							
						c+=1
					#print '------------End------------'
					#print 'result :',readonly
				
	return lists
