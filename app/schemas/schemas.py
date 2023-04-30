from pydantic import BaseSettings, BaseModel
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Settings(BaseSettings):
    SERVER_HOST: str
    SERVER_PORT: int


settings = Settings()


class Data(BaseModel):
    data = str

    class Config:
        orm_mode = True
