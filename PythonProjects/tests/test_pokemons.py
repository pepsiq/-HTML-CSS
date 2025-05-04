import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3af02c099eb9d65c8f1b00de089c5592'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 29634

def test_status_code():
    response = requests.get(url= f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_city():
    response_get = requests.get(url= f'{URL}/pokemons', params= {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Сарделька' ### уточнение имени покемона, не было в дз, но мне понравилась эта практика

    @pytest.mark.parametrize('key, value', [('name', 'Сарделька'), ('trainer_id', TRAINER_ID), ('id', '307571')])
    def test_parametrize(key, value):
        response_parametrize = requests.get(url= f'{URL}/pokemons', params= {'trainer_id': TRAINER_ID})
        assert response_parametrize.json()["data"][0][key] == value

def test_name():
    response_name = requests.get(url= f'{URL}/trainers{29634}', params= {'trainer_id': TRAINER_ID})
    

    @pytest.mark.parametrize('key, value', [('name', 'PepsiQ'), ('trainer_id', TRAINER_ID)])
    def test_name(key, value):
        response_name = requests.get(url= f'{URL}/trainers{29634}', params= {'trainer_id': TRAINER_ID})
        assert response_name.json()["data"][0][key] == "PepsiQ" ### уточнение имени тренера, уже было в дз
