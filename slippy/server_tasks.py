import aiofiles
import asyncio
import asyncore

import os


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


async def get_tail(filename):
    async with aiofiles.open(filename, mode='r') as f:
        lines = await tail(f)
        if lines:
            line = lines[0]
            return line.strip()


async def check_for_messages(filename):
    results = await get_tail(filename)
    return results
