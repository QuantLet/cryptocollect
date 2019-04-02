import json
from pymongo import MongoClient
import websocket
import datetime

mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['cryptocurrency']
poloniex_coll = db['poloniex']

currencies = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def millisec():
    tmp = datetime.datetime.now()
    return  tmp.timestamp()


def on_message(mes):
    message = json.loads(mes)
    if message[2][0] == 121:
        if message[2][1] != currencies[0]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "c": "BTC-USD", "t": millisec()}
            res = poloniex_coll.insert_one(result)
            print(datetime.datetime.now())
            print(result)
            currencies[0] = message[2][1]
            print(currencies)
    
    if message[2][0] == 122:
        if message[2][1] != currencies[1]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "c": "DASH-USD", "t": millisec()}
            res = poloniex_coll.insert_one(result)
            print(datetime.datetime.now())
            print(result)
            currencies[1] = message[2][1]
            print(currencies)
    
    if message[2][0] == 123:
        if message[2][1] != currencies[2]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "c": "LTC-USD", "t": millisec()}
            res = poloniex_coll.insert_one(result)
            print(datetime.datetime.now())
            print(result)
            currencies[2] = message[2][1]
            print(currencies)

    if message[2][0] == 126:
        if message[2][1] != currencies[3]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "c": "XMR-USD", "t": millisec()}
            res = poloniex_coll.insert_one(result)
            print(datetime.datetime.now())
            print(result)
            currencies[3] = message[2][1]
            print(currencies)

    if message[2][0] == 127:
        if message[2][1] != currencies[4]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "c": "XRP-USD", "t": millisec()}
            res = poloniex_coll.insert_one(result)
            print(datetime.datetime.now())
            print(result)
            currencies[4] = message[2][1]
            print(currencies)

    if message[2][0] == 149:
        if message[2][1] != currencies[5]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "c": "ETH-USD", "t": millisec()}
            res = poloniex_coll.insert_one(result)
            print(datetime.datetime.now())
            print(result)
            currencies[5] = message[2][1]
            print(currencies)

    if message[2][0] == 173:
        if message[2][1] != currencies[6]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "c": "ETC-USD",
                      "t": millisec()}
            res = poloniex_coll.insert_one(result)
            print(datetime.datetime.now())
            print(result)
            currencies[6] = message[2][1]
            print(currencies)

    if message[2][0] == 235:
        print("received BCH")
        if message[2][1] != currencies[7]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "c": "BCH-USD",
                      "t": millisec()}
            res = poloniex_coll.insert_one(result)
            print(datetime.datetime.now())
            print(result)
            currencies[7] = message[2][1]
            print(currencies)

    if message[2][0] == 203:
        if message[2][1] != currencies[8]:
            result = {"p": message[2][1], "lowest_ask": message[2][2], "highest_bid": message[2][3], "c": "EOS-USD",
                      "t": millisec()}
            res = poloniex_coll.insert_one(result)
            print(datetime.datetime.now())
            print(result)
            currencies[8] = message[2][1]
            print(currencies)


ws = websocket.WebSocketApp('wss://api2.poloniex.com')

ws.on_open = lambda self: self.send('{ "command": "subscribe", "channel": 1002 }')

ws.on_close = lambda self: self.send('{ "command": "subscribe", "channel": 1002 }')

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)