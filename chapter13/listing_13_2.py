'''
Завершение подпроцесса
'''
import asyncio
from asyncio.subprocess import Process
from sys import platform


async def main():
    if platform == 'linux' or platform == 'linux2':
        process: Process = await asyncio.create_subprocess_exec('sleep', 3)
    elif platform == 'win32':
        process: Process = await asyncio.create_subprocess_exec('cmd', 'start', '/wait',
                                                                'timeout', '3')
        print(f'pid процесса {process.pid}')
        try:
            status_code = await asyncio.wait_for(process.wait(), timeout=1.0)
            print(status_code)
        except asyncio.TimeoutError:
            print('Тайм-фут, завершаю принудительно...')
            process.terminate()
            status_code = await process.wait()
            print(status_code)


asyncio.run(main())
