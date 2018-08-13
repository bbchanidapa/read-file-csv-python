import os,pprint,re
x = {'t1':1, 't2':2, 'at' : 3}
# del x['t1']
# print x

# result = re.match('\w+t'or't\w+', 'sstasa')
# a = result.group()
# print result,a

types = ['INTEGER','INTEGER','VARCHAR']
data = ['2','5','c']

print data


# for c in h:		
count = len(types)
for i in range(0,count):	
	if types[i] == 'INTEGER':
		data[i] = int(data[i])
		print i,data
	else:
		print 'str'

	
