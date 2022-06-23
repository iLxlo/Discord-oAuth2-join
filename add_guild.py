import pymongo
import dns
import time
from oauth import Oauth
cluster = pymongo.MongoClient("")
db = cluster["data"]
collection = db["tokens"]
s = 0
codes = collection.find({})
for i in codes:
  s += 1
print(f"user count: {s}")
server_id = int(input("server id:"))
amount = int(input("amount:"))
password = str(input("password:"))
if password == "password":
    s = 0
    tokens = collection.find({})
    for i in range(0,int(amount)):
        try:
            user_id = Oauth.get_user_json(tokens[i]["token"])["id"]
            username = Oauth.get_user_json(tokens[i]["token"])["username"]
            Oauth.add_to_guild(tokens[i]["token"], user_id,server_id)
            s +=1
            print(username)
            time.sleep(2)
        except:
            print("error")
    print("done")
