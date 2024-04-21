import json
from typing import Any
import requests
import uvicorn
from fastapi import FastAPI, Request
import uuid

app = FastAPI()


@app.get("/token/{authorization_data}")
async def read_item(authorization_data: str):
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    payload='scope=GIGACHAT_API_PERS'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': str(uuid.uuid4()),
    'Authorization': f'Basic {authorization_data}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    return response.text


@app.post("/chat/completions/{token}")
async def read_item(token: str, req: Request):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    payload = await req.json()
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload), verify=False)
    return response.text

if __name__ == "__main__":
    uvicorn.run("main:app")