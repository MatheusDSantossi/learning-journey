from fastapi import FastAPI, Response, Cookie
from typing import Optional

app = FastAPI()

@app.get("/set-cookie")
def set_cookie_endpoint(response: Response):
    response.set_cookie(key="my_cookie", value="hello_world_fastapi")
    return {"message": "Cookie 'my_cookie' has been set."}

@app.get("/get-cookie")
def get_cookie_endpoint(my_cookie: Optional[str] = Cookie(None)):
    if (my_cookie):
        return {"message": f"Value of 'my_cookie': {my_cookie}"}
    else:
        return {"message": "Cookie 'my_cookie' not found."}
