'''
Использование исполнителя пула потоков совместно
с asyncio
'''
import asyncio
import functools
import requests
from concurrent.futures import ThreadPoolExecutor
from util import async_timed


def get_status_code(url: str) -> int:
    responce = requests.get(url)
    return responce.status_code


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        urls = ['https://www.example.com' for _ in range(1000)]
        tasks = [loop.run_in_executor(pool,
                                      functools.partial(get_status_code, url)) for url in
                 urls]
        results = await asyncio.gather(*tasks)
        print(results)


asyncio.run(main())
