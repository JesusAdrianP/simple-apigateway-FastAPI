import json
from trie import Trie


def get_data_from_json_file(file_path: str) -> dict[str, dict]:
    """ Load JSON data from a file and return it as a dictionary. """
    
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data


def resorce_path_identifier_to_service_map(urls_config: dict) -> dict[str, str]:
    """ Creates a mapping of resource path identifiers to corresponding service names. """
    
    return {value["resource_path_identifier"]: key for key, value in urls_config.items()}


def generate_trie_for_resorce_path_identifiers(urls_config: dict) -> Trie:
    """ Generate a Trie data structure for resource path identifiers. """

    trie = Trie()
    for service_data in urls_config.values():

        resorce_path = service_data["resource_path_identifier"]     
        trie.insert(resorce_path)

    return trie

        

def resolve_mircroservice_url(target_url: str,
                              resources_services_map: dict[str, str],
                              urls_config: dict[str, dict],
                              url_path_trie: Trie
                              ) -> str | None:
    """ 
    Resolve a microservice URL based on the target URL.

    If i client makes a reques to 
        http://gateway-url.com/users/api/token
    
    Then the values pass in the target_ulr should be
        /users/api/token

    
    Then return values will be the service url that matches the pattern
    in the target_url, so if there is a service that does this, the fucntion
    will return something like this.

        http://some-service.com/users/api/token

    In case that none of the service int he ulrs_config mathces the target url
    the fucntion will return None

    """
    
    search_result = url_path_trie.longest_matched_string(target_url)

    try:
        print(target_url)
        service_name = resources_services_map[search_result]
    
    except KeyError:
        return None


    service_url = urls_config[service_name]['url']

    return service_url + target_url

