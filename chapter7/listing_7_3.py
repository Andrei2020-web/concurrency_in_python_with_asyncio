'''
Базовое использование requests
'''
import requests
import time


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


start = time.time()

urls = ['https://www.example.com' for _ in range(1000)]

for url in urls:
    print(get_status_code(url))

end = time.time()

print(f'Выполнение запросов завершено за {end - start:.4f} c.')
