import json
from pymongo import MongoClient
from websocket import WebSocketApp
import datetime

mongo_client = MongoClient('mongodb://dataadmin:daPknihTi7@localhost/cryptocurrency')
db = mongo_client['cryptocurrency']
hitbtc_coll = db['hitbtc']

def on_message(mes):
    #print(mes)
    message = json.loads(mes)
    result = {'_id': message['params']['data'][0]['id'], 'p': message['params']['data'][0]['price'], 'q': message['params']['data'][0]['quantity'], 'side': message['params']['data'][0]['side'], 't': message['params']['data'][0]['timestamp'], 'c': message['params']['symbol']}
    print(datetime.datetime.now())
    print(result)
    res = hitbtc_coll.insert_one(result)

ws = WebSocketApp('wss://api.hitbtc.com/api/2/ws')

ws.on_open = lambda self: self.send(json.dumps({
    "method": "subscribeTrades",
    #"product_ids": ["BTC-USD", "ETH-USD", "LTC-USD"],
    "params":
        {
            "symbol": "BTCUSD"
        }
    }))

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)