
from paises import get_regions, get_country_by_region, encode_sha1


#=============================InicioTest
#PROBANDO LA FUNCIÓN obtener_regiones
regions = []
headers = {"x-rapidapi-host": "restcountries-v1.p.rapidapi.com","x-rapidapi-key": "138bf105acmsh9559d0aa02b5a31p15c933jsn73b13c1900e8"}
response = requests.get('https://restcountries-v1.p.rapidapi.com/all', headers=headers)
response = response.json()
#=============================FinTest


#=============================InicioTest
regions = get_regions()
print("hola bb function get_regions")
print(regions)
#=============================FinTest

#=============================InicioTest
obj = encode_sha1("jelou", encoding='utf-8')
print("hola bb sha")
print(obj)
#=============================FinTest

#=============================InicioCuerpoFunción
# -------------- test with less information
# crear una lista de diccionarios de paises
print(response)
print('hola bebe linda')
country_a = response[3]
print(country_a['languages'][0])
short_response = [{'name': country['name'], 'language': country['languages'], 'region': country['region']} \
                    for country in response]

#'language': encode_sha1(res[0]['languages'][0]['name'])

# verificando tipos, ambos son listas
print(type(regions))
print(type(short_response))

# imprimiendo los 5 primeros paises
for country in short_response[:5]:
    print(country)

# crear un diccionario q tiene como clave la region
# y como valor una lista vacia donde se agregaran los paises
countries_x_region = {}
# countries_x_region = [{'Asia': ['japn', 'korea']}, {'Europe': []}, {'Africa': []}, {'Oceania': []}, {'Americas': []}, {'Polar': []}]

for country in short_response:
    for region in regions:
        if country['region'] == region:
            countries_x_region[region] = country
countries_x_region['time'] = (1.5-1)*1000
print('country_x_region')
print(countries_x_region)
#=============================FinCuerpoFunción

#=============================InicioTest
countries = get_country_by_region(regions)
print("hola bb function get_country_by_regions")
print(countries)
#=============================FinTest