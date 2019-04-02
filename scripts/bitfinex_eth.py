import json
from pymongo import MongoClient
import websocket
import datetime

mongo_client = MongoClient('mongodb://dataadmin:daPknihTi7@35.204.101.74:27017/cryptocurrency')
db = mongo_client['cryptocurrency']
bitfinex_coll = db['bitfinex']

def on_message(mes):
    print(datetime.datetime.now())
    print("Bitfinex - 6 - ETH-USD:" + " " + mes)
    message = json.loads(mes)
    if message[1] in ('tu'):
        result = {'_id': message[2][0], 't': message[2][1], 'v': message[2][2], 'p': message[2][3],
                  'c': 'ETH-USD'}
        res = bitfinex_coll.insert_one(result)


ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "trades", "symbol": "tETHUSD"}')

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)