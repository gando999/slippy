import aiohttp
from aiohttp import web


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            if msg.data == 'updates':
                print('Received message')
                ws.send_str('this is an update')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed {}'.format(ws.exception()))

    print('websocket closed')

    return ws


def init_func(argv):
    app = web.Application()
    app.router.add_get('/', websocket_handler)
    return app
