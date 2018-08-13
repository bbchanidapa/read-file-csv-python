import os

filename = os.listdir('.')
listfile = filename
count = len(listfile)
path = "t.py"

print filename

for x in xrange(0,count):
	file = listfile[x]
	if file == 'config.py':
	 	print 'filename is : '+ file
	elif file == 't.csv':
		print 'filename is : '+ file
	elif file == 't.py':
		print 'filename is : '+ file
	else :
		pass
	
