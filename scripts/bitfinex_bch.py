import json
from pymongo import MongoClient
import websocket
import time

mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['cryptocurrency']
bitfinex_coll = db['bitfinex']

def on_message(mes):
    print(mes)
    message = json.loads(mes)

    # if message['event'] not in ('subscribed'):
    #     print('error received in BCH:' + ' ' + message['event'])
    #     time.sleep(3)
    #     ws.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBCHUSD"}')
    #     print('resubscribing')

    if message[1] in ('tu'):
        print(message[2])
        result = {'_id': message[2][0], 't': message[2][1], 'v': message[2][2], 'p': message[2][3],
                  'c': 'BCH-USD'}
        res = bitfinex_coll.insert_one(result)

def on_close(evt):
    print('not today!')
    ws.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBCHUSD"}')


ws = websocket.WebSocketApp('wss://api-pub.bitfinex.com/ws/2')

ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBCHUSD"}')

ws.on_message = lambda self, evt: on_message(evt)

ws.on_close = lambda self: self.send('{ "event": "subscribe", "channel": "trades", "symbol": "tBCHUSD"}')

# ws.on_error = lambda self, evt: on_error(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)