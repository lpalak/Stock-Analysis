from textblob import TextBlob
import json
import statistics

from pymongo import MongoClient

# Create a MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')

# Connect to the Database and it's collection
db = client.project.stocks

map = open('map.js', 'r').read()
reduce = open('reduce1.js', 'r').read()

client.project.messages_grouped.drop()
db.map_reduce(map, reduce, "messages_grouped")

results = client.project.messages_grouped.find()


data = []
for record in results:
    symbol = ''+record['value']['key']
    data = record['value']['value']
    buyCount = 0
    sellCount = 0
    for i in data:
        testimonial = TextBlob(i)
        if testimonial.sentiment.subjectivity > 0.3:
            buyCount += 1
        else:
            sellCount += 1

    total = buyCount+sellCount
    buyPercent = (buyCount*100)/total
    sellPercent = (sellCount*100)/total
    with open("format.json") as json_file:
        json_data = json.load(json_file)

    json_data['data']['content'][0]['value'] = buyPercent
    json_data['data']['content'][1]['value'] = sellPercent

    with open(symbol+'.json', 'w') as outfile:
        json.dump(json_data, outfile)