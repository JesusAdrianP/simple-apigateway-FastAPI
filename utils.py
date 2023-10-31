import json




def get_data_from_json_file(file_path: str) -> dict[str, dict]:
    
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data


def resorce_path_identifier_to_service_map(urls_config: dict) -> dict[str, str]:
    
    return {value["resource_path_identifier"]: key for key, value in urls_config.items()}



def resolve_mircroservice_url(target_url: str,
                              resources_services_map: dict[str, str],
                              urls_config: dict[str, dict]
                              ) -> str | None:
    
    url_parts = target_url.split('/')
    url_parts = url_parts[1:]

    path_identifier = url_parts[0]
    try:
        print(path_identifier)
        service_name = resources_services_map[path_identifier]
    except KeyError:
        return None


    service_url = urls_config[service_name]['url']

    return service_url + target_url


        
# URLS_JSON_FILE = './urls_config.json'

# URLS_CONFIG = get_data_from_json_file(URLS_JSON_FILE)

# RESORCES_TO_SERVICES = resorce_path_identifier_to_service_map(URLS_CONFIG)
    
# url = resolve_mircroservice_url(target_url='/users/api/token',
#                                     resources_services_map= RESORCES_TO_SERVICES,
#                                     urls_config= URLS_CONFIG
#                                     )

    

# print(url)