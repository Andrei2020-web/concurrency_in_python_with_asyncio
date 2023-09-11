'''
Использование блокировок с целью избежать
состояния гонки
'''
import asyncio
from asyncio import Lock


class MockSocket:
    def __init__(self):
        self.socket_closed = False

    async def send(self, msg: str):
        if self.socket_closed:
            raise Exception('Сокет закрыт!')
        print(f'Отправляется: {msg}')
        await asyncio.sleep(1)
        print(f'Отправлено: {msg}')

    def close(self):
        self.socket_closed = True


user_names_to_socket = {'John': MockSocket(),
                        'Terry': MockSocket(),
                        'Graham': MockSocket(),
                        'Eric': MockSocket()}


async def user_disconnect(username: str, user_lock: Lock):
    print(f'{username} отключен!')
    # Захватить блокировку, перед тем как удалять пользователя и закрывать сокет
    async with user_lock:
        print(f'{username} удаляется из словаря')
        socket = user_names_to_socket.pop(username)
        socket.close()


async def message_all_users(user_lock: Lock):
    print('Создаются задачи отправки сообщений')
    async with user_lock:
        messages = [socket.send(f'Привет, {user}')
                    for user, socket in user_names_to_socket.items()]
        await asyncio.gather(*messages)


async def main():
    user_lock = Lock()
    await asyncio.gather(message_all_users(user_lock), user_disconnect('Eric', user_lock))


asyncio.run(main())
