import requests, json

movie_db_api_key = '9d2c939718d281ff45061117c43b057a'

params = {
    'api_key': movie_db_api_key,
}
response = requests.get(url='https://api.themoviedb.org/3/movie/19995', params=params)
response.raise_for_status()
data = response.json()

print(json.dumps(data, indent=4))

'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/3npygfmEhqnmNTmDWhHLz1LPcbA.jpg'