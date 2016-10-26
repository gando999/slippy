import aiohttp
from aiohttp import web
import asyncio

from slippy.server_tasks import check_for_messages


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            if msg.data == 'initialise':
                print('Initialising client connection')
                buff = []
                while True:
                    messages = await check_for_messages()
                    for message in messages:
                        if message not in buff:
                            ws.send_str(message)
                            buff.append(message)
                    await asyncio.sleep(2)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('websocket connection closed {}'.format(ws.exception()))
    print('websocket closed')
    
    return ws


def init_func(argv):
    app = web.Application()
    app.router.add_get('/', websocket_handler)
    return app
