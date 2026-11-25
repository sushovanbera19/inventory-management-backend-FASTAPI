from fastapi import FastAPI

from database import Base, engine
from Models import user_model
from Routes import user_routes

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Register user routes
app.include_router(
    user_routes.router,
    prefix="/api"
)



@app.get("/")
def home():
    return {"message": "Inventra Backend is running!"}