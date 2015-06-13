

from pymongo import MongoClient
from bson.objectid import ObjectId
#from pymongo import Code

#import statistics

#print(statistics.mean([1, 2, 3, 4, 4]))


#print(statistics.median([1, 3, 5]))
#print(statistics.mode([1, 1, 2, 3, 3, 3, 3, 4]))
#print(statistics.pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

#data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
#print(statistics.variance(data))

#print(statistics.stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

#print('------------------------------------------------------------------------')

connection = MongoClient("mongodb://localhost:27017/")

db = connection.DataStorage.bData

#for doc in db.find({"items.name":"server"}):
 #     print(doc)

#collection = db.find({"_id" : ObjectId("556186b0f95f252050c872ef")})

map = open('map.js','r').read()
reduce = open('reduce1.js','r').read()

results = db.map_reduce(map,reduce,"posts_123")

for result in results.find():
    print("--> ",result['_id'],result['value'])