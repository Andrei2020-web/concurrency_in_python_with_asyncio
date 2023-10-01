'''
Сокеты и будущие объекты
'''
import functools
import selectors
import socket
from listing_14_5 import CustomFuture
from selectors import BaseSelector


def accept_connection(future: CustomFuture, connection: socket):
    # Установить сокет для чтения-записи данных в будущем объекте, когда придет
    # запрос на подключение от клиента
    print(f'Получен запрос на подключение от {connection}')
    future.set_result(connection)


async def sock_accept(sel: BaseSelector, sock) -> socket:
    # Зарегистрировать в селекторе функцию accept_connection и приостановиться
    # в ожидании запроса на подключение
    print('Регистрируется сокет для прослушивания подключений')
    future = CustomFuture()
    sel.register(sock, selectors.EVENT_READ, functools.partial(accept_connection, future))
    print('Прослушиваю запросы на подключение...')
    connection: socket = await future
    return connection


async def main(sel: BaseSelector):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 8000))
    sock.listen()
    sock.setblocking(False)

    print('Ожидаю подключения к сокету!')
    connection = await sock_accept(sel, sock)
    print(f'Получено подключение {connection}!')


selector = selectors.DefaultSelector()

coro = main(selector)

while True:
    # В бесконечном цикле вызывать метод send главной сопрограммы. При каждом событии
    # селектора выполнять зарегистрированный обратный вызов
    try:
        state = coro.send(None)
        events = selector.select()

        for key, mask in events:
            print('Обрабатываются события селектора...')
            callback = key.data
            callback(key.fileobj)
    except StopIteration as si:
        print('Приложение завершилось!')
        break
