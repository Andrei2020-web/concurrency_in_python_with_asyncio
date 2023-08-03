'''
Приложение для нагрузочного тестирования
'''
import asyncio
from asyncio import AbstractEventLoop
from threading import Thread
from chapter7.listing_7_11 import LoadTester


class ThreadedEventloop(Thread):
    '''
    Класс потока, в котором будет крутиться цикл событий asyncio
    '''

    def __init__(self, loop: AbstractEventLoop):
        super().__init__()
        self._loop = loop
        self.daemon = True

    def run(self):
        self._loop.run_forever()


loop = asyncio.new_event_loop()

asyncio_thread = ThreadedEventloop(loop)
asyncio_thread.start()

app = LoadTester(loop)
app.mainloop()
