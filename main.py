from fastapi import FastAPI, HTTPException, Request
from proxy_manager import reverse_proxy
from  utils import get_data_from_json_file, resorce_path_identifier_to_service_map


app = FastAPI()

URLS_JSON_FILE = './urls_config.json'

URLS_CONFIG = get_data_from_json_file(URLS_JSON_FILE)

RESORCES_TO_SERVICES = resorce_path_identifier_to_service_map(URLS_CONFIG)


# Define a function to proxy requests
# async def proxy_request(target_url: str, request: Request) -> httpx.Request:
#     async with httpx.AsyncClient() as client:
#         response = await client.request(
#             method=request.method,
#             url=target_url,
#             headers=dict(request.headers),
#             content=request.stream(),
#         )
    
#     try:
#         json_response = response.json()
#     except ValueError:
#         # Handle JSON parsing errors here
#         json_response = {}

#     return json_response, response.status_code, response.headers


# def resolve_mircroservice_url(target_url: str, urls_config: dict):
#     url_parts = target_url.split('/')
#     url_parts = url_parts[1:]
    




@app.get("/")
def read_root():
    return {"Hello": "mundo"}



# async def reverse_proxy(request: Request):
#     # print(request['headers'])
#     # print(dict(request))
#     # body = await request.body()
#     # print(body)

#     url = 'http://127.0.0.1:8000' + request['path']

#     print('hola mundooooo 1')

#     content, status, headers = await proxy_request(url, request)

#     print('hola mundooooo 2')

#     # print(type(content))
#     # print(content)

#     # print(status," ", type(status))
#     # print(url)
#     # print(request['path'])
#     # print(request['path'].startswith('/users'))

#     resolve_mircroservice_url(request['path'], urls_config)


#     return JSONResponse(content=content, status_code=status, headers=headers)

app.add_route("/{path:path}", reverse_proxy, ["GET", "POST", "PUT", "PATCH", "DELETE"])