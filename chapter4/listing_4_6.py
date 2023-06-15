'''
Завершение допускающих ожидание объектов
не по порядку
'''
import asyncio
from util import delay


async def main():
    result = await asyncio.gather(delay(3), delay(1))
    print(result)


asyncio.run(main())
