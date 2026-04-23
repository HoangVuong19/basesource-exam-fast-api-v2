from .healthcheck_router import router as healthcheck_router
from .category_router import router as category_router

all_router = [healthcheck_router, category_router]
