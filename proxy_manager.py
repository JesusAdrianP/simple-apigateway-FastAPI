import httpx
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from utils import resolve_mircroservice_url

# Define a function to proxy requests
async def make_request(target_url: str, request: Request) -> httpx.Request:
    async with httpx.AsyncClient() as client:

        try:
            response = await client.request(
                method=request.method,
                url=target_url,
                headers=dict(request.headers),
                content=request.stream(),
            )

            response.raise_for_status()
            
        except httpx.ConnectError as e:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Service unavailable")
        except httpx.HTTPError as e:
            # print(dir(e))
            # print(dir(e.response))
            # print(e.response.stream)
            # print(e.response.reason_phrase)
            # print(e.response.json)

            status_code = e.response.status_code
            error_message = e.response.reason_phrase
            raise HTTPException(status_code=status_code, detail=error_message)
      
    
    
    try:
        json_response = response.json()
    except ValueError:
        # Handle JSON parsing errors here
        json_response = {}

    return json_response, response.status_code, response.headers


async def reverse_proxy(request: Request):
    from main import URLS_CONFIG, RESORCES_TO_SERVICES
    # print(request['headers'])
    # print(dict(request))
    # body = await request.body()
    # print(body)

    url = 'http://127.0.0.1:8000' + request['path']
    url = resolve_mircroservice_url(target_url=request['path'],
                                    resources_services_map= RESORCES_TO_SERVICES,
                                    urls_config= URLS_CONFIG
                                    )

    print('hola mundooooo 1')
    print(url)


    content, status, headers = await make_request(url, request)

    print('hola mundooooo 2')

    # print(type(content))
    # print(content)

    # print(status," ", type(status))
    # print(url)
    # print(request['path'])
    # print(request['path'].startswith('/users'))

    return JSONResponse(content=content, status_code=status, headers=headers)
    
