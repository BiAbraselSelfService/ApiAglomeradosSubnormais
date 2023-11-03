from fastapi import FastAPI

app = FastAPI()

#main
@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}