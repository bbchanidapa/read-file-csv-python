import os,csv

read_file = os.listdir('.')
count = len(read_file)
name_to_db = []
data_ipphone= []
a = []
for x in range(0,count):
	cut_name = read_file[x]
	_fist = cut_name[0:-22]
	_last = cut_name[-22:]
	if _fist == 'cdr_tel_':
		cdr_tel_ = _fist+_last
		name_to_db.append(cdr_tel_)
		c_tel = _fist
		open_file  = open(cdr_tel_)
		reader = csv.reader(open_file)
		data_tel = []
		for row in reader:
			data_tel = row
		else:
			pass
			open_file.close()
    #-------------if--------------
	elif _fist == 'cdr_StandAloneCluster_':
		cdr_StandAloneCluster_ = _fist+_last
		name_to_db.append(cdr_StandAloneCluster_)
		
		a.append(cdr_StandAloneCluster_)
		open_file  = open(cdr_StandAloneCluster_,'r')
		reader = csv.reader(open_file)
		

		for row in reader:
			data = row
		else:
			data_ipphone.append(data)

			open_file.close()
	#-------------ElseIf--------------	
	else:
		pass

else:	
	pass

