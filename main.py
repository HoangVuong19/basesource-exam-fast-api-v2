from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from configs.env import get_settings
from routers import all_router
from middlewares.request_middleware import RequestMiddleware

settings = get_settings()

app = FastAPI(title=settings.app_name, version=settings.api_version)

# includes all routers of the app
for router in all_router:
    app.include_router(router, prefix=settings.api_prefix, tags=["REST"])

# add middlewares
__MIDDLEWARES__ = [RequestMiddleware]

for middleware in __MIDDLEWARES__.__reversed__():
    app.add_middleware(middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
