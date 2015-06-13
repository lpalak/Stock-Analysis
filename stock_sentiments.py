import urllib2
import json

from pymongo import MongoClient

# Create a MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')

# Connect to the Database and it's collection
db = client.project.stocks

fileOpen = open('company.txt')
## Read the first line
line = fileOpen.readline()


while line:
    print(line.rstrip())
    companyName = 'https://api.stocktwits.com/api/2/streams/symbol/'+line.rstrip()+'.json'
    print(companyName)
    response = urllib2.urlopen(companyName)
    data = json.load(response)
    db.insert(data)
    line = fileOpen.readline()

fileOpen.close()

results = db.find()

print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
for record in results:
   print(record['symbol']['symbol'])

print()

client.close()

