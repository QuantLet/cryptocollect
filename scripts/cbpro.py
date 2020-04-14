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
cbpro_coll = db['cbpro']

def on_message(mes):
    #print(mes)
    message = json.loads(mes)
    if message['type'] in ('last_match', 'match'):
        print(datetime.datetime.now())
        print(message)
        result = {"_id": message['trade_id'], "maker_order_id": message['maker_order_id'], "taker_order_id": message['taker_order_id'], "side": message['side'], "q": message['size'], "p": message['price'], "s": message['product_id'], "t": message['time'], 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
        res = cbpro_coll.insert_one(result)

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