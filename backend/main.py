from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello!"}


@app.get("/info")
def info():
    return {"info": [1, 2, 3]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)