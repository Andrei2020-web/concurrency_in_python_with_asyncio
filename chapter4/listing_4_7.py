'''
Использование as_completed
'''
import asyncio
import aiohttp
from util import async_timed
from chapter4 import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'http://www.example.com', 1),
                    fetch_status(session, 'http://www.example.com', 1),
                    fetch_status(session, 'http://www.example.com', 10)]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())
