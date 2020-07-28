from fastapi import FastAPI  

app = FastAPI()

@app.get("/")
def get_spotify():
    return {"FastAPI": "Working"}