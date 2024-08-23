from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from .docs import *
from config.database import Base, engine

def get_server():
    server = FastAPI(
        title='MSA & DDD Study', 
        docs_url="/docs", redoc_url=None,
        version="1.0.2",
        description=root_description,
        openapi_url="/openapi.json"
    )
    server.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    server.add_middleware(
        GZipMiddleware, minimum_size=1000
    )

    return server


# 테이블 생성
Base.metadata.create_all(bind=engine)

app = get_server()

@app.get('/', tags=['Root'])
def ping():
    return 201