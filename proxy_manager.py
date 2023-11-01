import httpx
from fastapi import HTTPException, Request, status, Response
from utils import resolve_mircroservice_url


def convert_httpx_response_to_fastapi_response(httpx_response: httpx.Response) -> Response:
    """Converts a httpx.Response object to a FastAPI Response object."""

    status_code = httpx_response.status_code
    headers = httpx_response.headers
    content = httpx_response.content
    media_type = headers["Content-Type"]

    fastapi_response = Response(
        status_code= status_code,
        content= content,
        headers= headers,
        media_type= media_type
    )

    return fastapi_response


# Define a function to proxy requests
async def make_request(url: str, request: Request) -> httpx.Response:
    """ 
    Asynchronously make an HTTP request to the specified URL.

    Raises:
        HTTPException: If there is an issue with the HTTP request, such as invalid URL, 
        connection error, HTTP status code errors, or other exceptions.
    """

    async with httpx.AsyncClient() as client:

        try:
            response = await client.request(
                method=request.method,
                url=url,
                headers=dict(request.headers),
                content=request.stream(),
            )

            response.raise_for_status()
        
        except TypeError as e:
            print('utils.make_request TypeError')
            print(url)
            raise HTTPException(status_code=400, detail='Invalid type for url')

        except httpx.ConnectError as e:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Service unavailable")
        
        except httpx.HTTPError as e:
            print('utils.make_request  httpx.HTTPError')
            print(url)
            status_code = e.response.status_code
            error_message = e.response.reason_phrase
            raise HTTPException(status_code=status_code, detail=error_message)
      

    return response


async def reverse_proxy(request: Request) -> Response:
    """ 
    Reverse proxy handler that forwards an HTTP request to a microservice based on the request path.
    
    This function forwards the request to the appropriate microservice based on the request path,
    retrieves the response, and returns it as a FastAPI Response.

    Note: The function relies on external data loaded from the main module (URLS_CONFIG, RESORCES_TO_SERVICES, URL_PATHS_TRIE).
    
    """
    from main import URLS_CONFIG, RESORCES_TO_SERVICES, URL_PATHS_TRIE

    url = resolve_mircroservice_url(target_url=request['path'],
                                    resources_services_map= RESORCES_TO_SERVICES,
                                    urls_config= URLS_CONFIG,
                                    url_path_trie= URL_PATHS_TRIE
                                    )


    response = await make_request(url, request)

    fastapi_response = convert_httpx_response_to_fastapi_response(response)

    return fastapi_response
