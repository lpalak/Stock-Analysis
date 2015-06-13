import urllib2
import json
import csv

from pymongo import MongoClient

# Create a MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')

# Connect to the Database and it's collection
db = client.project.quotes

# Create the TSV file


results = db.find()

# For Closing Price
for record in results:
    data = record['query']['results']['row']
    fileName = record['query']['symbol']
    with open(fileName+'_closing.tsv', 'wb') as csvfile:
        fieldnames = ['date', 'close']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for i in data:
            writer.writerow({'date': ''+(str(i['col0'])), 'close': ''+(str(float(i['col6'])))})

results = db.find()
# For Volume
for record in results:
    data = record['query']['results']['row']
    fileName = record['query']['symbol']
    with open(fileName+'_volume.tsv', 'wb') as csvfile:
        fieldnames = ['date', 'volume']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for i in data:
            writer.writerow({'date': ''+(str(i['col0'])), 'volume': ''+(str(float(i['col5'])))})