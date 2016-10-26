import aiohttp
import asyncio


session = aiohttp.ClientSession()

async def run_client():
    async with session.ws_connect('http://localhost:8080') as ws:
        ws.send_str('updates')
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == 'this is an update':
                    print('Got update')
                else:
                    ws.send_str('updates')
            elif msg.type == aiohttp.WSMsgType.CLOSED:
                break
            elif msg.type == aiohttp.WSMsgType.ERROR:
                break

loop = asyncio.get_event_loop()
loop.run_until_complete(run_client())
