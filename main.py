from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from Routes import upload_routes
# model import
from Models import user_model
from Models import category_model
from Models import product_model
# routes import
from Routes import user_routes
from Routes import category_routes
from Routes import product_routes
from Routes import admin_category_routes


app = FastAPI()
# Static folder for uploaded images
UPLOAD_DIR = Path(__file__).resolve().parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app.mount(
    "/uploads",
    StaticFiles(directory=str(UPLOAD_DIR)),
    name="uploads"
)
# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,allow_origins=[
 # User Website
    "http://localhost:5180",
    "http://127.0.0.1:5180",

   # Admin Panel
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register user routes
app.include_router(user_routes.router, prefix="/api")
app.include_router(category_routes.router,prefix="/api")
app.include_router(product_routes.router, prefix="/api")
app.include_router(admin_category_routes.router, prefix="/api")
app.include_router(upload_routes.router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Inventra Backend is running!"}