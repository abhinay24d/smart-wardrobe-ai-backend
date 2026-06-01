from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routes.register_routes import router as register_router
from app.routes.theme_routes import router as theme_router
from app.routes.signup_routes import router as signup_router
from app.routes.login_routes import router as login_router
from app.routes.protected_routes import router as protected_router
from app.routes.outfit_routes import router as outfit_router
from app.routes.recommendation_routes import router as recommendation_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve uploaded images
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.get("/")
def home():
    return {
        "message": "Smart Wardrobe AI Backend Running"
    }


# Routes
app.include_router(signup_router)
app.include_router(login_router)
app.include_router(protected_router)
app.include_router(outfit_router)
app.include_router(recommendation_router)
app.include_router(register_router)
app.include_router(theme_router)