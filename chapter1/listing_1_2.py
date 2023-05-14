'''
Процессы и потоки в простом Python-приложении
'''
import os
import threading

print(f'Исполняется python-процесс с идентификатором: {os.getpid()}')
total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'В данный момент python исполняет {total_threads} поток(ов)')
print(f'Имя текущего потока {thread_name}')
