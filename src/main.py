from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.utils.database import Database
db = Database()

# 系統啟動時建立資料庫連線
@asynccontextmanager
async def lifespan(app: FastAPI):
  db.create_db_and_tables()
  yield
  db.engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.get('/')
def hello_world():
  return 'Hello, World!'
