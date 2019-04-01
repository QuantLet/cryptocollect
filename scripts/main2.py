import json
from pymongo import MongoClient
import websocket


mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['cryptocurrency']
cbpro_coll = db['cbpro']

# ws = websocket.create_connection("wss://ws-feed.pro.coinbase.com")
# ws.send(json.dumps({
#     "type": "subscribe",
#     #"product_ids": ["BTC-USD", "ETH-USD", "LTC-USD"],
#     "channels": [
#         {
#             "name": "matches",
#             "product_ids": [
#                 "BTC-USD",
#                 "ETH-USD"
#             ],
#         }
#     ]
# }))
#
#
# while True:
#     result_orig = ws.recv()
#     result = json.loads(result_orig)
#     print ("Received '%s'" % result)
#     #res = cbpro_coll.insert_one(result)
#     #print(res.inserted_id)
#     print('')
# ws.close()


def on_message(mes):
    print(mes)
    message = json.loads(mes)
    print(message)


ws = websocket.WebSocketApp('wss://ws-feed.pro.coinbase.com')

ws.on_open = lambda self: self.send(json.dumps({
    "type": "subscribe",
    #"product_ids": ["BTC-USD", "ETH-USD", "LTC-USD"],
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

ws.run_forever()