import json
from pymongo import MongoClient
import websocket
import datetime

from pathlib import Path

d = Path().resolve().parent

with open(str(d) + '/credentials.txt', 'r') as file:
    credentials = file.read().replace('\n', '')

mongo_client = MongoClient(credentials) # e.g. 'mongodb://localhost:27017'
db = mongo_client['cryptocurrency']
bitfinex_coll = db['bitfinex']

def on_message(mes):
    print(datetime.datetime.now())
    print("Bitfinex - 5 - ETC-USD:" + " " + mes)
    message = json.loads(mes)
    if message[1] in ('tu'):
        result = {'_id': message[2][0], 't': message[2][1], 'q': message[2][2], 'p': message[2][3],
                  's': 'ETC-USD', 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
        res = bitfinex_coll.insert_one(result)


ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "trades", "symbol": "tETCUSD"}')

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)