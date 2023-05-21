'''
Использование await для ожидания результата
сопрограммы.
Встретив выражение await, интерпретатор приостанавливает родительскую
сопрограмму и выполняет сопрограмму в выражении await. По ее завершении
родительская сопрограмма приостанавливается и возвращенное ей значение
присваивается переменной.
'''
import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def main() -> None:
    one_plus_one = await add_one(1)
    two_plus_one = await add_one(2)
    print(one_plus_one)
    print(two_plus_one)


asyncio.run(main())
