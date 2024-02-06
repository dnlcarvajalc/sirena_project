import requests
import json
import random
import constants

def do_get_request(request_argument):
    """Función que se encarga de realizar la petición GET a la API

    Args:
        request_argument (_type_): Complemento con query-parameters de la API

    Returns:
        _type_: Retorna el json que la API suministra
    """
    response = requests.get(f'{constants.BASE_URL}{request_argument}')
    return response

response = do_get_request(constants.request_argument)

def random_offset(response):
    """Función encargada de generar un número aleatorio dependiendo de la máxima 
        posición de registros suministrados por la API, luego inserta este número
        en el query-parameter "offset" y acceder a la información de este.

    Args:
        response (_type_): Recibe el json inicial para examinar el número máximo de
        posiciones inmerso en este. 
    """
    data = response.json()
    max_random_limit = data["metadata"]["totalCount"]
    random_number = random.randint(1,max_random_limit)

    new_request_argument = f"/v1/geo/places?limit=1&offset={random_number}"
    new_response = do_get_request(new_request_argument)
    if random_number > 0:
        print(json.dumps(new_response.json()["data"], indent=2))

random_offset(response)