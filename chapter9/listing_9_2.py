'''
Подключение к базе данных о товарах
'''
import asyncpg
from aiohttp import web
from aiohttp.web import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool
from typing import List, Dict

routes = web.RouteTableDef()
DB_KEY = 'database'


async def create_database_pool(app: Application):
    # Создать пул подключений к базе данных и сохранить его в экземпляре приложения
    print('Создаётся пул подключений.')
    pool: Pool = await asyncpg.create_pool(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='password',
        database='products',
        min_size=6,
        max_size=6,
    )
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application):
    # Уничтожить пул в экземпляре приложения
    print('Уничтожается пул подключений.')
    pool: Pool = app[DB_KEY]
    await pool.close()


@routes.get('/brands')
async def brands(request: Request) -> Response:
    # Запросить все марки и вернуть результаты клиенту
    connection: Pool = request.app[DB_KEY]
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results: List[Record] = await connection.fetch(brand_query)
    result_as_dict: List[Dict] = [dict(brand) for brand in results]
    return web.json_response(result_as_dict)


app = web.Application()
# Добавить сопрограммы создания и уничтожения пула в обработчики инициализации и очистки
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app)
