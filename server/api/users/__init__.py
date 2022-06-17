from starlette.routing import Route

from server.api.users.endpoints import Login, Register, Refresh

users_routes = [
    Route("/login", Login),
    Route("/register", Register),
    Route('/refresh', Refresh)
]
