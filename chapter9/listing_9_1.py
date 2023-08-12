'''
Оконечная точка для возврата текущего времени
'''
from aiohttp import web
from datetime import datetime
from aiohttp.web_request import Request
from aiohttp.web_response import Response

routes = web.RouteTableDef()


@routes.get('/time')
async def time(request: Request) -> Response:
    '''Создать конечную GET-точку time, когда клиент обратится к ней,
    будет вызвана сопрограмма time'''
    today = datetime.today()
    result = {
        'month': today.month,
        'day': today.day,
        'time': str(today.time())
    }
    return web.json_response(result)


# Создать веб-приложение, зарегистрировать маршруты и запустить его
app = web.Application()
app.add_routes(routes)
web.run_app(app)
