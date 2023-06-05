'''
Неправильное использование блокирующего API
как сопрограммы
'''
import asyncio
import requests
from util import async_timed


@async_timed()
async def get_example_status() -> int:
    return requests.get('http://www.ya.ru').status_code


@async_timed()
async def main():
    task1 = asyncio.create_task(get_example_status())
    task2 = asyncio.create_task(get_example_status())
    task3 = asyncio.create_task(get_example_status())
    await task1
    await task2
    await task3


asyncio.run(main())
