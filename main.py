
from quart import Quart, render_template, redirect, request
from oauth import Oauth
import requests
import pymongo
import time
import json
import discord
import discord.ext
from discord.utils import get
from discord.ext import commands
import dns
import asyncio
app = Quart('')
app.secret_key = 'BOT SECRET'
cluster = pymongo.MongoClient("YOUR MONGO DB")
db = cluster["data"]
collection = db["tokens"]
@app.before_serving
async def before_serving():
    loop = asyncio.get_event_loop()
    app.discord_client = Di.DiscordClient()
    await app.discord_client.bot.login("BOT TOKEN")
    loop.create_task(app.discord_client.bot.connect())

@app.route("/")
async def index():
    return redirect("REDIRECT URI")

@app.route("/login",methods=["get"])
async def login():
  try:
      code = request.args.get('code')
      info = Oauth.exchange_code(code)
      new_code = info["access_token"]
      print(new_code)
      refresh_code = info["refresh_token"]
      tokens = collection.find({})
      valid = False
      for i in tokens:
          if i["token"] == new_code:
              valid = True
              break
      if valid == False:
          collection.insert_one({"token":new_code,"refresh_token":refresh_code})
          username = Oauth.get_user_json(new_code)["username"]
          user_id = Oauth.get_user_json(new_code)["id"]
          await app.discord_client.add_role(user_id)
          requests.post("YOUR WEBHOOK FOR VERIFY LOG", data=json.dumps({"content":f"**{user_id}** verified!"}),headers={"Content-Type":"application/json"})
          return await render_template("login.html",username=username)
      else:
          username = Oauth.get_user_json(new_code)["username"]
          user_id = Oauth.get_user_json(new_code)["id"]
          await app.discord_client.add_role(int(user_id))
          
          return await render_template("login.html",username=username)
  except:
      return "error"
@app.route("/start")
async def start():
    await app.discord_client.start_status()
    return "ok"

def run():
  app.run(
    host='0.0.0.0',
    port=8000,
    debug=True
  )
if __name__ == "__main__":

    run()
