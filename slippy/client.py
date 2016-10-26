import aiohttp
import asyncio


session = aiohttp.ClientSession()

async def run_client():
    ws = await aiohttp.ws_connect('http://localhost:8080')
    print('Intialising client')
    while True:
        msg = await ws.receive()
        if msg.type == aiohttp.WSMsgType.TEXT:
            print(msg.data)
        elif msg.type == aiohttp.WSMsgType.CLOSED:
            break
        elif msg.type == aiohttp.WSMsgType.ERROR:
            break

loop = asyncio.get_event_loop()
loop.run_until_complete(run_client())
