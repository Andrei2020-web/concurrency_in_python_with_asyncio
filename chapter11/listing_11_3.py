'''
Использование блокировки asyncio
'''
import asyncio
from asyncio import Lock
from util import delay


async def a(lock: Lock):
    print('Сопрограмма а ждёт возможности захватить блокировку')
    async with lock:
        print('Сопрограмма а находится в критической секции')
        await delay(2)
    print('Сопрограмма а освободила блокировку')


async def b(lock: Lock):
    print('Сопрограмма b ждёт возможности захватить блокировку')
    async with lock:
        print('Сопрограмма b находится в критической секции')
        await delay(2)
    print('Сопрограмма b освободила блокировку')


async def main():
    lock = Lock()
    await asyncio.gather(a(lock), b(lock))


asyncio.run(main())
