import aiofiles
import asyncio
import asyncore

import os

READ_POLL = 2


interesting = []

loop = asyncio.get_event_loop()

async def tail(f, lines=1, _buffer=4098):
    lines_found = []
    block_counter = -1

    while len(lines_found) < lines:
        try:
            await f.seek(block_counter * _buffer, os.SEEK_END)
        except IOError:
            await f.seek(0)
            lines_found = await f.readlines()
            break
        lines_found = await f.readlines()
        if len(lines_found) > lines:
            break
        block_counter -= 1
    return lines_found[-lines:]


async def watch_logs():
    last_line = None
    while True:
        for filename in interesting:
            async with aiofiles.open(filename, mode='r') as f:
                lines = await tail(f)
                if lines:
                    line = lines[0]
                    if line != last_line and line.strip():
                        print(line.strip())
                        last_line = line
                await asyncio.sleep(READ_POLL)


loop.run_until_complete(watch_logs())
loop.close()
