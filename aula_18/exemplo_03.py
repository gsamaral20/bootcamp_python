import requests
from pydantic import BaseModel

#contrato de dados, schema de dados, a view da API
class PokemonScheme(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True

def pegar_pokemon(id: int) -> PokemonScheme:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    data_types = data['types'] # suponde que data é o dicionário com os dados
    types_list = []

    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonScheme(name = data['name'], type = types)

if __name__ == "__main__":
    print(pegar_pokemon(10))
    print(pegar_pokemon(32))
    print(pegar_pokemon(155))
