from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import HTMLResponse, Response

from some_http.db import GAMES, USERS

app = FastAPI()


class Game(BaseModel):
    name: str
    price: str


@app.get("/", response_class=HTMLResponse)
def index():
    with open('static/index.html') as f:
        return f.read()


@app.get("/admin", response_class=HTMLResponse)
def admin():
    with open('static/admin.html') as f:
        return f.read()


@app.get("/games")
def get_games():
    return GAMES


@app.post("/games")
def add_games(game: Game, username: str, password: str):
    print(username, password)
    for user in USERS:
        if user["username"] == username and user["password"] == password:
            GAMES.append(game.dict())
            return Response(status_code=204)
    return Response("Wrong username or password", status_code=401)
