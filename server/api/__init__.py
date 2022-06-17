from starlette.routing import Mount

from server.api.users import users_routes

api_routes = [
    Mount("/users", routes=users_routes)
]