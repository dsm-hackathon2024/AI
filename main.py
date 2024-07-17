from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origin = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 추가
from src.quest import router as data_router
from src.gpt import router as prompt_router

app.include_router(data_router, prefix="/data")
app.include_router(prompt_router, prefix="/prompt")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=4292, reload=True)
