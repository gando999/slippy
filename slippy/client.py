import aiohttp
import argparse
import asyncio


async def get_ws_connection(stackname):
    while True:
        try:
            ws = await aiohttp.ws_connect(
                'http://{}:8080'.format(stackname)
            )
            return ws
        except aiohttp.errors.ClientOSError:
            print('Failed to get connection')
            await asyncio.sleep(5)


async def run_client(stackname):
    ws = await get_ws_connection(stackname)
    print('Intialising client')
    while True:
        msg = await ws.receive()
        if msg.type == aiohttp.WSMsgType.TEXT:
            print(msg.data)
        elif msg.type == aiohttp.WSMsgType.CLOSED:
            break
        elif msg.type == aiohttp.WSMsgType.ERROR:
            break


parser = argparse.ArgumentParser()
parser.add_argument('stackname')
args = parser.parse_args()

loop = asyncio.get_event_loop()
loop.run_until_complete(run_client(args.stackname))
