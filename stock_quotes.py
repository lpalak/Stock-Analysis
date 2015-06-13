import urllib2
import json

from pymongo import MongoClient

# Create a MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')

# Connect to the Database and it's collection
db = client.project.quotes

fileOpen = open('company.txt')
## Read the first line
line = fileOpen.readline()


db.remove({})
while line:
    print line.rstrip()
    companyName = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20csv%20where%20url%3D%27http%3A%2F%2Fichart.finance.yahoo.com%2Ftable.csv%3Fs%3D'+line.rstrip()+'%26a%3D1%26b%3D1%26c%3D2015%26d%3D4%26e%3D28%26f%3D2015%26g%3Dd%27&format=json&diagnostics=true&callback='
    print companyName
    response = urllib2.urlopen(companyName)
    data = json.load(response)
    data['query']['symbol'] = line.rstrip()
    data['query']['results']['row'].pop(0)
    db.insert(data)
    line = fileOpen.readline()

fileOpen.close()
