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
poloniex_coll = db['poloniex']


currencies = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def on_message(mes):
    message = json.loads(mes)
    print(message)
    if message[2][0] == 121:
        if message[2][1] != currencies[0]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "s": "BTC-USD", "t": datetime.datetime.utcnow(), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
            print(result)
            res = poloniex_coll.insert_one(result)
            currencies[0] = message[2][1]
            print(currencies)
    
    if message[2][0] == 122:
        if message[2][1] != currencies[1]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "s": "DASH-USD", "t": datetime.datetime.utcnow(), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
            res = poloniex_coll.insert_one(result)
            print(result)
            currencies[1] = message[2][1]
            print(currencies)
    
    if message[2][0] == 123:
        if message[2][1] != currencies[2]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "s": "LTC-USD", "t": datetime.datetime.utcnow(), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
            res = poloniex_coll.insert_one(result)
            print(result)
            currencies[2] = message[2][1]
            print(currencies)

    if message[2][0] == 126:
        if message[2][1] != currencies[3]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "s": "XMR-USD", "t": datetime.datetime.utcnow(), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
            res = poloniex_coll.insert_one(result)
            print(result)
            currencies[3] = message[2][1]
            print(currencies)

    if message[2][0] == 127:
        if message[2][1] != currencies[4]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "s": "XRP-USD", "t": datetime.datetime.utcnow(), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
            res = poloniex_coll.insert_one(result)
            print(result)
            currencies[4] = message[2][1]
            print(currencies)

    if message[2][0] == 149:
        if message[2][1] != currencies[5]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "s": "ETH-USD", "t": datetime.datetime.utcnow(), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
            res = poloniex_coll.insert_one(result)
            print(result)
            currencies[5] = message[2][1]
            print(currencies)

    if message[2][0] == 173:
        if message[2][1] != currencies[6]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "s": "ETC-USD",
                      "t": datetime.datetime.utcnow(), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
            res = poloniex_coll.insert_one(result)
            print(result)
            currencies[6] = message[2][1]
            print(currencies)

    if message[2][0] == 235:
        print("received BCH")
        if message[2][1] != currencies[7]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "s": "BCH-USD",
                      "t": datetime.datetime.utcnow(), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
            res = poloniex_coll.insert_one(result)
            print(result)
            currencies[7] = message[2][1]
            print(currencies)

    if message[2][0] == 203:
        if message[2][1] != currencies[8]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "s": "EOS-USD",
                      "t": datetime.datetime.utcnow(), 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
            res = poloniex_coll.insert_one(result)
            print(result)
            currencies[8] = message[2][1]
            print(currencies)


ws = websocket.WebSocketApp('wss://api2.poloniex.com')

ws.on_open = lambda self: self.send('{ "command": "subscribe", "channel": 1002 }')

ws.on_close = lambda self: self.send('{ "command": "subscribe", "channel": 1002 }')

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)