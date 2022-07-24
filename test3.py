import pymongo

#client is the connection to mongodb
client = pymongo.MongoClient("mongodb+srv://majahar84639:majahar84639@majahar.oghvp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["Myinfo"]
collection = database["majahar"]

'''record = collection.find()
for i in record:
    print(i)
'''
'''data = collection.find({"companyName": "iNeuron"})
for i in data:
    print(i)'''

data = collection.find({"courseOffered": {"$gt" :"E"}})
for i in data:
    print(i)