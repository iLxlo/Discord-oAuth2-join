import pymongo
import dns
import time
from oauth import Oauth
cluster = pymongo.MongoClient("mongodb+srv://discord:oauth2@cluster0.7t74z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["data"]
collection = db["tokens"]
s = 0
k = 0
tokens = collection.find({})
for i in tokens:
  try:
      username = Oauth.get_user_json(i["token"])["id"]
      print(username)
      s +=1
      time.sleep(2)
  except:
      print("error")
      k +=1
      collection.delete_one({"token" : i["token"]})
print(s,k)