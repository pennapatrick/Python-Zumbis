import requests
url = 'https://rickandmortyapi.com/api/character/2'
data = requests.get(url).json()
print(data['name'], '//', data['status'], )
