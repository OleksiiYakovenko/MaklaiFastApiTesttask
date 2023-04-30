from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from app.schemas.schemas import settings
from app.routes.routes import router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)