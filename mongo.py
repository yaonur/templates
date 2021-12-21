from pymongo import MongoClient

conn_ebrand = 'mongodb://root:profiterol@mongo-primary.collector-tr.svc.cluster.local:27017,mongo-secondary.collector-tr.svc.cluster.local:27017/?authSource=admin&replicaSet=rs-collector-tr&readPreference=nearest&appname=MongoDB%20Compass&ssl=false'
conn_str = 'mongodb://localhost:27017'
client = MongoClient(conn_str)
client_ebrand = MongoClient(conn_ebrand)
dbs = client.list_databases()

db = client.pinterest
collection = db.keywords
keywords = list(collection.find())
for item in keywords[0:5]:
    print(item)
