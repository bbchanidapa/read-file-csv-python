x = {'title1','title2'}
y = {5,10}
#x.update({3:4})
#print x

a = {1,2}

y.update(a)


zips = dict(zip(x,y))
print zips
print y,zips

#y['data'] = dict(x)
