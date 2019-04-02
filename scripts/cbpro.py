import json
from pymongo import MongoClient
from websocket import WebSocketApp
import datetime

mongo_client = MongoClient('mongodb://dataadmin:daPknihTi7@35.204.101.74:27017/cryptocurrency')
db = mongo_client['cryptocurrency']
cbpro_coll = db['cbpro']

def on_message(mes):
    #print(mes)
    message = json.loads(mes)
    if message['type'] in 'last_match':
        print(datetime.datetime.now())
        print(message)
        res = cbpro_coll.insert_one(message)

ws = WebSocketApp('wss://ws-feed.pro.coinbase.com')

ws.on_open = lambda self: self.send(json.dumps({
    "type": "subscribe",
    "channels": [
        {
            "name": "matches",
            "product_ids": [
                "BTC-USD",
                "ETH-USD",
                "LTC-USD",
                "XRP-USD",
                "BCH-USD",
                "XLM-USD",
                "ZRX-USD"
            ],
        }
    ]
}))

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)