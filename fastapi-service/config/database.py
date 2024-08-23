from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from starlette.config import Config

config = Config('fastapi-service/.env')

# DB_URL='mysql+pymysql://root:12345678@db:3306/sample'
DB_URL=f'mysql+pymysql://' + config('MARIADB_ID') + ":" + config('MARIADB_ROOT_PASSWORD') + "@mariadb:" + config('MARIADB_SERVER_PORT') + "/" + config('MAREADB_DATABASE')

# 엔진 생성
engine = create_engine(DB_URL, echo=True)   # echo=True : 실행되는 SQL 쿼리 확인

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 베이스 클래스 생성
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()