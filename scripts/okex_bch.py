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
    if message[0]['data'][0][4] in ['bid', 'ask']:
        result = {'_id': message[0]['data'][0][0], 'p': message[0]['data'][0][1], 'q': message[0]['data'][0][2],
                  't': datetime.datetime.utcnow(), 'side': message[0]['data'][0][4], 's': 'BCH-USD', 'date': datetime.datetime.utcnow().strftime('%Y-%m-%d')}
        print(datetime.datetime.now())
        print(result)
        res = okex_coll.insert_one(result)


ws = WebSocketApp('wss://real.OKEx.com:8443/ws/v3')

ws.on_open = lambda self: self.send(json.dumps({
    "event": "addChannel",
    "channel": "ok_sub_spot_bch_usdt_deals"
}))

ws.on_message = lambda self, evt: on_message(evt)

ws.run_forever(ping_interval=10, ping_timeout=5)

print(datetime.datetime.now())
