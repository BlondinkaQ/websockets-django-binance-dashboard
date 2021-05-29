import json
from random import randint
import time
from binance.client import Client
import asyncio
from binance import AsyncClient, BinanceSocketManager
from datetime import datetime, timedelta


from channels.generic.websocket import AsyncWebsocketConsumer


class WSConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

        client = await AsyncClient.create()
        bm = BinanceSocketManager(client)
        async with bm.kline_socket(symbol='BTCUSDT', interval='5m') as stream:
            while True:
                res = await stream.recv()
                api_key = 'xsB5mdl4aNvyWlOlByBO8VmThW5EI3b81MGNXq6TTpEwZ5PYRjedxzM7S8DN4CPd'
                api_secret_key = 'vSkMlwg8OGDm0UFdkYa2rYWUnYEh0RsrqspAn5BZctprCmTWGy3MFtgOfeqsB0q6'
                client_syn = Client(api_key, api_secret_key)
                client_syn.API_URL = 'https://testnet.binance.vision/api'

                date_kyiv = datetime.fromtimestamp(int(res['E']) / 1000).strftime('%d.%m.%Y %H:%M:%S')
                klines_nine_ago = client_syn.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_5MINUTE, "50 min ago UTC")
                moving_average = sum(float(klines_nine_ago[i][4]) for i in range(9)) / 9
                balance_btc = client_syn.get_asset_balance(asset='BTC')
                balance_usdt = client_syn.get_asset_balance(asset='USDT')


                await self.send(json.dumps({'bal_btc':balance_btc['free'],
                                            'bal_usdt':balance_usdt['free'],
                                            'ma': moving_average,
                                            'ct':date_kyiv,
                                            'cb': res['k']['c']}))






'''
        api_key = 'xsB5mdl4aNvyWlOlByBO8VmThW5EI3b81MGNXq6TTpEwZ5PYRjedxzM7S8DN4CPd'
        api_secret_key = 'vSkMlwg8OGDm0UFdkYa2rYWUnYEh0RsrqspAn5BZctprCmTWGy3MFtgOfeqsB0q6'


        client = Client(api_key, api_secret_key)

        client.API_URL = 'https://testnet.binance.vision/api'


        while True:

            info = client.get_asset_balance(asset='BTC')
            print(info)
            info1 = client.get_asset_balance(asset='USDT')
            print(info1)
            int(time.time() * 1000) - client.get_server_time()['serverTime']
            klines_nine_ago = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_5MINUTE, "50 min ago UTC")
            moving_average = sum(float(klines_nine_ago[i][4]) for i in range(9)) / 9
            print(moving_average)

            self.send(json.dumps({'mes': info['free'], 'ma': moving_average, 'mes1': info1['free']}))


'''


