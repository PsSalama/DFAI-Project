from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World11"}

@app.post("/register")
def register():
    return {"Hello": "World12"}