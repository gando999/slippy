import aiohttp
from aiohttp import web
import asyncio
from threading import Thread

from slippy.server_tasks import check_for_messages


loop = asyncio.get_event_loop()

interesting = []


async def start_checks(q, filename):
    while True:
        message = await check_for_messages(filename)
        await q.put(message)
        await asyncio.sleep(2)
    

def listen(q=None):
    if q is None:
        q = asyncio.Queue()
    for filename in interesting:
        loop.create_task(start_checks(q, filename))
    return q
    

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    q = listen()

    seen = []

    while True:
        msg = await q.get()
        if msg is None:
            break
        else:
            if msg not in seen:
                ws.send_str(msg)
                seen.append(msg)

    await ws.close()
    return ws


def init_func(argv):
    app = web.Application()
    app.router.add_get('/', websocket_handler)
    return app
