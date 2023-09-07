'''
Тестирование сопрограммы retry
'''
import asyncio
from chapter10.listing_10_7 import retry, TooManyRetries


async def main():
    async def always_fail():
        raise Exception('Грохнулась!')

    async def always_timeout():
        await asyncio.sleep(1)

    try:
        await retry(always_fail,
                    max_retries=3,
                    timeout=0.1,
                    retry_interval=0.1)
    except TooManyRetries:
        print('Слишком много попыток!')

    try:
        await retry(always_timeout,
                    max_retries=3,
                    timeout=0.1,
                    retry_interval=0.1)
    except TooManyRetries:
        print('Слишком много попыток!')


asyncio.run(main())
