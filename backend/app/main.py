import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .config.settings import settings
from .routes import auth_routes, voucher_routes, plan_routes, admin_routes, reseller_routes, router_routes, analytics_routes
from .config.database import engine, Base
from .models import user, voucher, plan, router, session, transaction, device

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

# Mount static files
# The structure is: root/backend/app/main.py
# Frontend is at: root/frontend
# So we need to go up 3 levels from main.py to reach root, then into frontend
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
frontend_path = os.path.join(base_dir, "frontend")

app.mount("/css", StaticFiles(directory=os.path.join(frontend_path, "css")), name="css")
app.mount("/js", StaticFiles(directory=os.path.join(frontend_path, "js")), name="js")
app.mount("/assets", StaticFiles(directory=os.path.join(frontend_path, "assets")), name="assets")

@app.get("/")
async def root():
    return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/{page}.html")
async def get_page(page: str):
    file_path = os.path.join(frontend_path, f"{page}.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "Page not found"}

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # This will create all tables if they don't exist
        await conn.run_sync(Base.metadata.create_all)

# Include routers
app.include_router(auth_routes.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(voucher_routes.router, prefix=f"{settings.API_V1_STR}/vouchers", tags=["vouchers"])
app.include_router(plan_routes.router, prefix=f"{settings.API_V1_STR}/plans", tags=["plans"])
app.include_router(admin_routes.router, prefix=f"{settings.API_V1_STR}/admin", tags=["admin"])
app.include_router(reseller_routes.router, prefix=f"{settings.API_V1_STR}/resellers", tags=["resellers"])
app.include_router(router_routes.router, prefix=f"{settings.API_V1_STR}/routers", tags=["routers"])
app.include_router(analytics_routes.router, prefix=f"{settings.API_V1_STR}/analytics", tags=["analytics"])
