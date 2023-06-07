'''
Запуск сервера и прослушивание порта
для подключения
'''
import socket

# Создать TCP-сервер
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Задать адрес сокета
server_address = ('127.0.0.1', 8000)

# Прослушивать запросы на подключение
server_socket.bind(server_address)
server_socket.listen()

# Дождаться подключения и выделить клиенту сокет
connection, client_address = server_socket.accept()
print(f'Получен запрос на подключение от {client_address}!')

