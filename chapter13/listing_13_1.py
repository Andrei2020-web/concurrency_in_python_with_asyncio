'''
Выполнение простой команды в подпроцессе
'''
import asyncio
from asyncio.subprocess import Process
from sys import platform


async def main():
    if platform == 'linux' or platform == 'linux2':
        process: Process = await asyncio.create_subprocess_exec('ls', '-l')
    elif platform == 'win32':
        process: Process = await asyncio.create_subprocess_exec('cmd', '/c dir')
    print(f'pid процесса: {process.pid}')
    status_code = await process.wait()
    print(f'Код состояния: {status_code}')


asyncio.run(main())
