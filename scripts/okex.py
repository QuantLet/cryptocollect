import json
import zlib
from pymongo import MongoClient
from websocket import WebSocketApp
import datetime

mongo_client = MongoClient('mongodb://dataadmin:daPknihTi7@localhost/cryptocurrency')
db = mongo_client['cryptocurrency']
okex_coll = db['okex']

def inflate(data):
    decompress = zlib.decompressobj(
            -zlib.MAX_WBITS  # see above
    )
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated

def on_message(mes):
    mes = inflate(mes)
    #print(mes)
    message = json.loads(mes, encoding = 'utf-8')
    # print(message['table'])
    if message['table'] in ['spot/ticker']:
        #print(message['data'][0])
        result = {'p': message['data'][0]['last'], 'q': message['data'][0]['last_qty'],
                  't': message['data'][0]['timestamp'], 's': message['data'][0]['instrument_id'], 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
        print(datetime.datetime.now())
        print(result)
        res = okex_coll.insert_one(result)


ws = WebSocketApp('wss://real.OKEx.com:8443/ws/v3')

ws.on_open = lambda self: self.send(json.dumps(
    {"op": "subscribe", "args": ["spot/ticker:BTC-USDT","spot/ticker:BCH-USDT","spot/ticker:ETC-USDT","spot/ticker:ETH-USDT","spot/ticker:LTC-USDT"]}
))

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)