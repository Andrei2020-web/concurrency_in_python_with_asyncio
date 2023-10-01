'''
Использование объекта CustomFuture в цикле
'''
from listing_14_5 import CustomFuture

future = CustomFuture()

i = 0

while True:
    try:
        print('Проверяется будущий объект...')
        gen = future.__await__()
        gen.send(None)
        print('Будущий объект не готов...')
        if i == 1:
            print('Устанавливается значение будущего объекта...')
            future.set_result('Готово!')
        i += 1
    except StopIteration as si:
        print(f'Значение равно: {si.value}')
        break
