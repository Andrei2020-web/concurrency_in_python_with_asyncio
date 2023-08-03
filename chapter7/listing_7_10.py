'''
Класс нагрузочного тестирования
'''
import asyncio
from concurrent.futures import Future
from asyncio import AbstractEventLoop
from typing import Callable, Optional
from aiohttp import ClientSession


class StressTest:

    def __init__(self,
                 loop: AbstractEventLoop,
                 url: str,
                 total_requests: int,
                 callback: Callable[[int, int], None]):
        self._completed_requests: int = 0
        self._load_test_future: Optional[Future] = None
        self._loop = loop
        self._url = url
        self._total_request = total_requests
        self._callback = callback
        self._refresh_rate = total_requests // 100

    def start(self):
        # Начать отправку запросов и сохранить будущий объект, чтобы впоследствии можно
        # было отменить тест
        future = asyncio.run_coroutine_threadsafe(self._make_requests(), self._loop)

    def cancel(self):
        if self._load_test_future:
            # Чтобы отменить тест, нужно вызвать метод cancel объекта _load_test_future
            self._loop.call_soon_threadsafe(self._load_test_future.cancel)

    async def _get_url(self, session: ClientSession, url: str):
        try:
            await session.get(url)
        except Exception as e:
            print(e)
        self._completed_requests = self._completed_requests + 1
        # После того как отправка 1 % запросов завершена, вызвать функцию обратного
        # вызова, передав ей число завершенных запросов и общее число запросов
        if self._completed_requests % self._refresh_rate == 0 \
                or self._completed_requests == self._total_request:
            self._callback(self._completed_requests, self._total_request)

    async def _make_requests(self):
        async with ClientSession() as session:
            reqs = [self._get_url(session, self._url) for _ in range(self._total_request)]
        await asyncio.gather(*reqs)
