from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Inventra Backend is running!"}