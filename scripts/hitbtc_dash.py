import json
from pymongo import MongoClient
from websocket import WebSocketApp
import datetime

from pathlib import Path

d = Path().resolve().parent

with open(str(d) + '/credentials.txt', 'r') as file:
    credentials = file.read().replace('\n', '')

mongo_client = MongoClient(credentials) # e.g. 'mongodb://localhost:27017'
db = mongo_client['cryptocurrency']
hitbtc_coll = db['hitbtc']

def on_message(mes):
    #print(mes)
    message = json.loads(mes)
    result = {'_id': message['params']['data'][0]['id'], 'p': message['params']['data'][0]['price'], 'q': message['params']['data'][0]['quantity'], 'side': message['params']['data'][0]['side'], 't': message['params']['data'][0]['timestamp'], 's': message['params']['symbol'], 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
    print(datetime.datetime.now())
    print(result)
    res = hitbtc_coll.insert_one(result)

ws = WebSocketApp('wss://api.hitbtc.com/api/2/ws')

ws.on_open = lambda self: self.send(json.dumps({
    "method": "subscribeTrades",
    #"product_ids": ["BTC-USD", "ETH-USD", "LTC-USD"],
    "params":
        {
            "symbol": "DASHUSD"
        }
    }))

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)