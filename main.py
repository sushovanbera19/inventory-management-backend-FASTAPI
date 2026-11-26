from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
# model import
from Models import user_model
from Models import category_model
# routes import
from Routes import user_routes
from Routes import category_routes

app = FastAPI()
# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,allow_origins=[
 # User Website
    "http://localhost:5180",
    "http://127.0.0.1:5180",

    # Admin Panel
    "http://localhost:5174",
    "http://127.0.0.1:5174"
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


def home():
    return {"message": "Inventra Backend is running!"}