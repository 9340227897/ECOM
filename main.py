from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from user import route as UsersRoute
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()


app.mount("/static", StaticFiles(directory="user/static"), name="static")

app.include_router(UsersRoute.router)


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)



