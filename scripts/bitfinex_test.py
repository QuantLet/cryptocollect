import json
from pymongo import MongoClient
import websocket
import datetime

mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['cryptocurrency']
bitfinex_coll = db['bitfinex']

### BTC ###
def on_message(mes):
    #print(mes)
    message = json.loads(mes)
    if message[1] in ('tu'):
        print(message[2])
        result = {'_id': message[2][0], 't': message[2][1], 'v': message[2][2], 'p': message[2][3],
                  'c': 'BTC-USD'}
        res = bitfinex_coll.insert_one(result)


ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBTCUSD"}')

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)

### LTC ###
def on_message2(mes):
    #print(mes)
    message = json.loads(mes)
    if message[1] in ('tu'):
        print(message[2])
        result = {'_id': message[2][0], 't': message[2][1], 'v': message[2][2], 'p': message[2][3],
                  'c': 'LTC-USD'}
        res = bitfinex_coll.insert_one(result)


ws2 = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws2.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "trades", "symbol": "tLTCUSD"}')

ws2.on_message = lambda self, evt: on_message2(evt)

ws2.run_forever(ping_interval=10, ping_timeout=5)

### ETH ###
def on_message3(mes):
    #print(mes)
    message = json.loads(mes)
    if message[1] in ('tu'):
        print(message[2])
        result = {'_id': message[2][0], 't': message[2][1], 'v': message[2][2], 'p': message[2][3],
                  'c': 'ETH-USD'}
        res = bitfinex_coll.insert_one(result)


ws3 = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws3.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "trades", "symbol": "tETHUSD"}')

ws3.on_message = lambda self, evt: on_message3(evt)

ws3.run_forever(ping_interval=10, ping_timeout=5)