import aiohttp
import asyncio


session = aiohttp.ClientSession()

async def run_client():
    async with session.ws_connect('http://localhost:8080') as ws:
        ws.send_str('initialise')
        print('Intialising client')
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                print(msg.data)
            elif msg.type == aiohttp.WSMsgType.CLOSED:
                break
            elif msg.type == aiohttp.WSMsgType.ERROR:
                break

loop = asyncio.get_event_loop()
loop.run_until_complete(run_client())
