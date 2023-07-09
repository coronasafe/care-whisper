from dotenv import dotenv_values
from starlette.applications import Starlette
from starlette.routing import Route
import uvicorn

from routes import ping, health_check

config = dotenv_values(".env")


BASE_URL = "/api/conversation/"

routes = [
    Route(BASE_URL+"ping", ping, methods=["GET"]),
    Route(BASE_URL+"health-check", health_check, methods=["GET"]),
]

app = Starlette(debug=True, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
