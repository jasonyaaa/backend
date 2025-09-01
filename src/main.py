from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

from src.auth.router import router as auth_router
from src.auth.admin_router import router as admin_router
from src.therapist.router import router as therapist_router
from src.course.router import router as course_router
from src.practice.routers.sessions_router import router as practice_sessions_router
from src.practice.routers.recordings_router import router as practice_recordings_router
from src.practice.routers.chapters_router import router as practice_chapters_router
from src.practice.routers.therapist_router import router as therapist_practice_router
from src.pairing.router import router as pairing_router
from src.verification.router import router as verification_router
from src.chat.router import router as chat_router
#建立一個chat router 並且重新 import as 別的名稱，不要混在一起
from src.ai_analysis.routers.management_router import management_router

# 系統啟動時建立資料庫連線
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield



app = FastAPI(
    title="VocalBorn API",
    version="1.0.0",
    contact={
        "name": "VocalBorn 開發團隊",
    },
    description="照上面你的網址去選要哪個Server",
    servers=[
        {
            "url": "https://api-vocalborn.r0930514.work",
        }, 
        {
            "url": "http://localhost",
        },
        {
            "url": "http://localhost:8000",
        },
        {
            "url": "https://vocalborn.r0930514.work/api",
        }
    ],
    lifespan=lifespan
)
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(therapist_router)
app.include_router(course_router)
app.include_router(practice_sessions_router)
app.include_router(practice_recordings_router)
app.include_router(practice_chapters_router)
app.include_router(therapist_practice_router)
app.include_router(pairing_router)
app.include_router(verification_router)
app.include_router(chat_router)
app.include_router(management_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return 'Hello, World!'
