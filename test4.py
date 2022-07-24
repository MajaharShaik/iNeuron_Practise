import pymongo
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

client = pymongo.MongoClient("mongodb+srv://majahar84639:majahar84639@majahar.oghvp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["Inventory"]
collection = database["Table"]
#collection.insert_many(data)

#This query is to collect all the data in the collection
'''d = collection.find()
for i in d:
    print(i)'''

#This query is to collect  data in the collection where status is "A"
'''d = collection.find({"status":"A"})
for i in d:
    print(i)'''

#This query is to collect  data in the collection where status is "A" or "P"
'''d = collection.find({"status":{"$in":["A","P"]}})
for i in d:
    print(i)'''

#This query is to collect  data in the collection where status is greterthan "C"
'''d = collection.find({"status":{"$gt":"C"}})
for i in d:
    print(i)'''

#This query is to collect  data in the collection where quantity is 100
'''d = collection.find({"qty":100})
for i in d:
    print(i)'''

#This query is to collect  data in the collection where quantity is greaterthen 75
'''d = collection.find({"qty":{"$gt":75}})
for i in d:
    print(i)'''

#This query is to collect  data in the collection where quantity is greaterthen or equal to  75
'''d = collection.find({"qty":{"$gte":75}})
for i in d:
    print(i)
'''

#This query is to collect  data in the collection where quantity is 95 and item is sketch pad
'''d = collection.find({'item': 'sketch pad','qty': 95})
for i in d:
    print(i)'''

# item = sketch pad and qty is greaterthan or equal to 75
'''d = collection.find({"item":"sketch pad","qty":{"$gte":75}})
for i in d:
    print(i)'''

# item = sketch pad or qty is greaterthan or equal to 75
'''d = collection.find({"$or":[{"item":"sketch pad","qty":{"$gte":75}}]})
for i in d:
    print(i)'''

#update item = canvas to majju
'''collection.update_one({'item': 'canvas'},{"$set":{"item":"majju"}})
d = collection.find()
for i in d:
    print(i)
'''

#deleting records
collection.delete_one({'item': 'majju'})
d = collection.find()
for i in d:
    print(i)