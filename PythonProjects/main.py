import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3af02c099eb9d65c8f1b00de089c5592'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Мяут",
    "photo_id": 1
}

body_new_name = {
    "pokemon_id": "307571",
    "name": "Сарделька",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "307571"
}

response_create = requests.post(url= f'{URL}/pokemons', headers= HEADER, json= body_create)
print(response_create.text)


message = response_create.json()['message']
print(message)


response_new_name = requests.put(url= f'{URL}/pokemons', headers= HEADER, json= body_new_name)
print(response_new_name.text)


response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_pokeball)
print(response_pokeball.text)