import json
from pymongo import MongoClient
import websocket
import datetime
import re

from pathlib import Path

d = Path().resolve().parent

with open(str(d) + '/credentials.txt', 'r') as file:
    credentials = file.read().replace('\n', '')

mongo_client = MongoClient(credentials) # e.g. 'mongodb://localhost:27017'
db = mongo_client['cryptocurrency']
bitstamp_coll = db['bitstamp']

def on_message(mes):
    message = json.loads(mes)
    if message['event'] in 'trade':
        result = {'_id': message['data']['id'], 'p': message['data']['price'], 'q': message['data']['amount'], 'sell_id': message['data']['sell_order_id'],
              'buy_id': message['data']['buy_order_id'], 'side': message['data']['type'], 't': message['data']['microtimestamp'], 's': re.sub('live_trades_', '', message['channel']), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
        print(datetime.datetime.now())
        print(result)
        res = bitstamp_coll.insert_one(result)


ws = websocket.WebSocketApp('wss://ws.bitstamp.net')

ws.on_open = lambda self: self.send('{ "event": "bts:subscribe", '
                                    '"data": {'
                                    '"channel": "live_trades_xrpusd"}}')

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)