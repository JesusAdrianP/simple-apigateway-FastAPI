from typing import Union
from fastapi import FastAPI, HTTPException, Request, Path
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()


# Define a function to proxy requests
async def proxy_request(target_url: str, request: Request) -> httpx.Request:
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=target_url,
            headers=dict(request.headers),
            content=request.stream(),
        )

    return response.text, response.status_code


@app.get("/")
def read_root():
    return {"Hello": "World"}



async def reverse_proxy(request: Request):
    print(request)
    print(dict(request))
    body = await request.body()
    print(body)
    return JSONResponse(content="alfhdakj", status_code=200)

app.add_route("/{path:path}", reverse_proxy, ["GET", "POST", "PUT", "PATCH", "DELETE"])