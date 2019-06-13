import tempfile
from aiohttp import web
import uvloop
from ctypes import cdll

uvloop.install()

app = web.Application()
routes = web.RouteTableDef()

@routes.post('/')
async def index(request):
    body = await request.read()
    with tempfile.NamedTemporaryFile() as f:
        print(body)
        f.write(body)
        code = cdll.LoadLibrary(f.name)
        out = code.run()
        return web.Response(text=str(out))

if __name__ == "__main__":
    app.add_routes(routes)
    web.run_app(app, host='0.0.0.0', port=5000)
