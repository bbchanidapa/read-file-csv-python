#-----------Doc insert----------
# dicts = {
# 	"name" : "P'OO",
# 	"age" : 10,
# 	"timestamp" : datetime.utcnow()
# }
#-----------move val------------
#db.table.remove({'name':'kk'})

#--------Insert--------#posts = nameCollection
# _id = table.insert_one(dicts).inserted_id
# print _id
# print table.find_one({ "_id" : _id }) 

#----------Find Tables----------
# cursor = table.find({}) 
# for document in cursor:
#     print(document)

#-----------Time stamp--------------
#({'timestamp': datetime.datetime.utcnow()})
#dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
#dt.strftime("%A, %d. %B %Y %I:%M%p")
#datetime.datetime.now(pytz.timezone('Asia/Jerusalem')).strftime('%z')
