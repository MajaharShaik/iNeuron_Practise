import pymongo

# This is MongoDb of my database
client = pymongo.MongoClient("mongodb+srv://majahar84639:majahar84639@majahar.oghvp.mongodb.net/?retryWrites=true&w=majority")
db = client.test


# MongoDb of iNeuron
#client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
#print(db)

d = {
    "name":"MAJAHAR",
    "email":"majahar84639@gmail.com",
    "surename":"SHAIK"
}

db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(d)