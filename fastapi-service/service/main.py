from fastapi import FastAPI

app = FastAPI()

@app.get('/', tags=['Root'])
def ping():
    return 200