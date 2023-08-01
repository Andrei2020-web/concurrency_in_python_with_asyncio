'''
Взаимоблокировка
'''
from threading import Lock, Thread
import time

lock_a = Lock()
lock_b = Lock()


def a():
    # Захватить блокировку а
    with lock_a:
        print('Захвачена блокировка а из метода а!')
        # Ждать одну секунду, это создает подходящие условия для взаимоблокировки
        time.sleep(1)
        with lock_b:
            print('Захвачена обе блокировки из метода а!')


def b():
    with lock_b:
        print('Захвачена блокировка b из метода b!')
        with lock_a:
            print('Захвачены обе блокировки из метода b!')


thread_1 = Thread(target=a)
thread_2 = Thread(target=b)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
