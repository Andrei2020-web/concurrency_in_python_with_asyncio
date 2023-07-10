'''
Перемещение по курсору и выборка записей
'''
import asyncpg
import asyncio


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='password'
    )

    async with connection.transaction():
        query = 'SELECT product_id, product_name FROM product'
        cursor = await connection.cursor(query)
        await cursor.forward(500)  # двинуть курсор вперёд на 500 записей
        products = await cursor.fetch(100)  # Получить следующие 100 записей
        for product in products:
            print(product)

    await connection.close()


asyncio.run(main())
