from fastapi import FastAPI, HTTPException, Request
from proxy_manager import reverse_proxy
from  utils import get_data_from_json_file, resorce_path_identifier_to_service_map


app = FastAPI()

URLS_JSON_FILE = './urls_config.json'

URLS_CONFIG = get_data_from_json_file(URLS_JSON_FILE)

RESORCES_TO_SERVICES = resorce_path_identifier_to_service_map(URLS_CONFIG)


@app.get("/")
def read_root():
    return {"Hello": "mundo"}


app.add_route("/{path:path}", reverse_proxy, ["GET", "POST", "PUT", "PATCH", "DELETE"])