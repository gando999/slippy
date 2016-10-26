import aiohttp
import asyncio


async def get_ws_connection():
    while True:
        try:
            ws = await aiohttp.ws_connect('http://localhost:8080')
            return ws
        except aiohttp.errors.ClientOSError:
            print('Failed to get connection')
            await asyncio.sleep(5)


async def run_client():
    ws = await get_ws_connection()
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
