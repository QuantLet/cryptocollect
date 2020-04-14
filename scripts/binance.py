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
binance_coll = db['binance']

def on_message(mes):
    print(mes)
    message = json.loads(mes)
    print(datetime.datetime.now())
    result = {'_id': message['t'], 't': message['T'], 's':  message['s'], 'p':  message['p'], 'q': message['q'],  'buyer_id':  message['b'],
              'seller_id':  message['a'], 'm':  message['m'], 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
    print(result)
    res = binance_coll.insert_one(result)
    #print("BTC-USD:" + " " + message)

ws = WebSocketApp('wss://stream.binance.com:9443/ws/bchusdt@trade/ltcusdt@trade/btcusdt@trade/eosusdt@trade/etcusdt@trade/ethusdt@trade/iotausdt@trade/xlmusdt@trade/xmrusdt@trade/xrpusdt@trade/zrxusdt@trade')

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)