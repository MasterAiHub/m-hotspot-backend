from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.settings import settings
from .routes import auth_routes, voucher_routes, plan_routes, admin_routes, reseller_routes, router_routes, analytics_routes

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/")
async def root():
    return {"message": "Welcome to M Hotspot API"}

# Include routers
app.include_router(auth_routes.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(voucher_routes.router, prefix=f"{settings.API_V1_STR}/vouchers", tags=["vouchers"])
app.include_router(plan_routes.router, prefix=f"{settings.API_V1_STR}/plans", tags=["plans"])
app.include_router(admin_routes.router, prefix=f"{settings.API_V1_STR}/admin", tags=["admin"])
app.include_router(reseller_routes.router, prefix=f"{settings.API_V1_STR}/resellers", tags=["resellers"])
app.include_router(router_routes.router, prefix=f"{settings.API_V1_STR}/routers", tags=["routers"])
app.include_router(analytics_routes.router, prefix=f"{settings.API_V1_STR}/analytics", tags=["analytics"])
