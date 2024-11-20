from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    password: str

@app.post("/register/")
def register(user: User):
    if user.name is not None and user.email is not None and user.password is not None:
        return {"message": "User successfully registered"}
    raise HTTPException(status_code=404, detail="Insufficient data")

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)