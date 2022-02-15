from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def lambda_handler():
    return {"message": "Hello World"}
