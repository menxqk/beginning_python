from pymongo import MongoClient
import datetime
import pprint

conn_str = 'mongodb://demo:demo@127.0.0.1:27017/demo'
client = MongoClient(conn_str)

# try:
#     print(client.server_info())
# except Exception:
#     print("Unable to connect to the server.")

db = client['demo']
people = db['people']
person = {"name": "John", "lastName": "Smith" }

ids = []
for i in range(0, 3):
    id = people.insert_one(person.copy()).inserted_id
    ids.append(id)
    print(type(id))
    pprint.pprint(id)
print()

pprint.pprint(people.find_one({"_id": id}))
print()

for id in ids:
    res = people.update_one({"_id": id}, {"$set": {"date": datetime.datetime.utcnow()}}).modified_count
    print('Updated:', res)
print()

for p in people.find():
    print(type(p))
    pprint.pprint(p)
print()

print('Total documents:', people.count_documents({}))
print()

for id in ids:
    res = people.delete_one({"_id": id}).deleted_count
    print('Deleted:', res)
print()

pprint.pprint(db.list_collection_names())

people.drop()

