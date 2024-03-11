from fastapi import FastAPI , Body
from pydantic import BaseModel



app : FastAPI = FastAPI(title="Hello World API", 
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])


@app.get("/")
def main_root() -> dict:
    '''This is a main route'''
    return {"Hello": "World"}

@app.get("/status")
def status_route() -> dict:
    '''This is a status route'''
    return {"status": "ok"}

@app.get("/hello")
def hello_user_route() -> dict:
    '''This is a hello user route'''
    return {"Hello": "Welcome"}

@app.get("/hello/{name}")
def hello_user_name_route(name: str) -> dict:
    '''This is a hello user name route'''
    return {"Hello": name}

@app.get("/notification/")
def notification_route(filter: str) -> dict:
    '''This is a notification route'''
    return {"Hello": filter}


class UserCreate(BaseModel):
    user_id: int
    username: str
    password: str
    
@app.post("/create_user/")
async def create_user(user_data: UserCreate):
    user_id = user_data.user_id
    username = user_data.username
    password = user_data.password
    return {
        "msg": "we got data succesfully",
        "user_id": user_id,
        "username": username,
        "password" :password
    }