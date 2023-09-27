'''
Использование communicate со стандартным вводом
'''
import asyncio
from asyncio.subprocess import Process


async def main():
    program = ['python', 'listing_13_3.py']
    process: Process = await asyncio.create_subprocess_exec(*program,
                                                            stdout=asyncio.subprocess.PIPE,
                                                            stdin=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate(b'Zoot')
    print(stdout)


asyncio.run(main())
