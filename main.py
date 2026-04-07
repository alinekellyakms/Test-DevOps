import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/helloword")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint( 0, 2000)}