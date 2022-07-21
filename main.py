import requests
from decorator import path_to_file
HOST = 'https://swapi.dev/api/'

@path_to_file('logs.txt')
def get_people(id):
    return requests.get(f'{HOST}people/{id}').json()

get_people(1)
get_people(2)
get_people(3)