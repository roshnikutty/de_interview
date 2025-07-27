import requests
import uvicorn

from fastapi import FastAPI, Header, HTTPException, status, Depends, Request
from typing import Optional

app = FastAPI()

API_KEY = "userorder123"
API_KEY_NAME = "X-API-Value"

headers = {
  "x-api-key": "X-API-Value"
}

@app.get('/')
def health_check():
  return 'I am healthy!'


def verify_api_key(
    x_api_key: Optional[str] = Header(None),
    request: Request = None
):

  api_key = x_api_key or request.query_params.get("cirkul") or request.query_params.get("api_key")
  if api_key != "userorder123" and api_key != "X-API-Value":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )


@app.get("/users", dependencies=[Depends(verify_api_key)])
async def get_users():
    # write code here - Get all users
      pass
      

# implement code below to get revenue by each user
# @app.get("/user-revenue", dependencies=[Depends(verify_api_key)])

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
