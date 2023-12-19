import os
from fastapi import FastAPI
from proxy_manager import reverse_proxy
from  utils import get_data_from_json_file, resorce_path_identifier_to_service_map, generate_trie_for_resorce_path_identifiers


app = FastAPI()

URLS_JSON_FILE = os.path.join('.', 'urls_config.json')

URLS_CONFIG = get_data_from_json_file(URLS_JSON_FILE)

RESORCES_TO_SERVICES = resorce_path_identifier_to_service_map(URLS_CONFIG)

URL_PATHS_TRIE = generate_trie_for_resorce_path_identifiers(URLS_CONFIG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar "*" con la URL específica de tu frontend en Render
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "from FastAPI gateway"}


app.add_route("/{path:path}", reverse_proxy, ["GET", "POST", "PUT", "PATCH", "DELETE"])
