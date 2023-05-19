'''
Многопоточное чтение кода состояния
'''
import time
import threading
import requests


def read_example() -> None:
    response = requests.get('https://www.ya.ru')
    print(response.status_code)


thread1 = threading.Thread(target=read_example)
thread2 = threading.Thread(target=read_example)

thread_start = time.time()

thread1.start()
thread2.start()

print('Все потоки работают!')

thread1.join()
thread2.join()

thread_end = time.time()

print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} c.')
