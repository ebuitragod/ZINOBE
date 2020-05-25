from hashlib import sha1

import json
import pandas as pd 
import requests
import timeit

#=============================GlobalVariables
#PROBANDO LA FUNCIÓN obtener_regiones
regions = []
headers = {"x-rapidapi-host": "restcountries-v1.p.rapidapi.com","x-rapidapi-key": "138bf105acmsh9559d0aa02b5a31p15c933jsn73b13c1900e8"}
response = requests.get('https://restcountries-v1.p.rapidapi.com/all', headers=headers)
response = response.json()
#=============================FinGlobalVariables

def get_regions():
    """
    Función para obtener las regiones de la api. 
    Punto 1:
    De https://rapidapi.com/apilayernet/api/rest-countries-v1, obtenga todas las regiones existentes.
    """
    regions = []
    for i in response:
        if i['region'] not in regions and i['region'] is not '':
            regions.append(i['region'])
    return regions


def encode_sha1(string, encoding='utf-8'):
    """
    Obteniendo el nombre del idioma en SHA1
    Punto 3:
    De https://restcountries.eu/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
    """
    try:
        res = sha1(string.encode(encoding)).hexdigest()
    except AttributeError:
        res = {'error': 'parameter provided is not a string'}
    return res

def get_country_by_region(region):
    """
    Vamos a obtener el primer país que se encuentre en la lista, por cada región. 
    Punto 2:
    De https://restcountries.eu/ Obtenga un pais por region apartir de la region optenida del punto 1.
    """
    initial_time = timeit.timeit()
    short_response = [{'name': country['name'], 'language': country['languages'], 'region': country['region']} \
                    for country in response]
    countries_by_region = {}
    final_time = timeit.timeit()
    total_time = (initial_time - final_time)*1000
    for country in short_response:
        for region in regions:
            if country['region'] == region:
                country['language'] = encode_sha1(country['language'][0])
                countries_by_region[region] = country
    countries_by_region['time'] = total_time

    return countries_by_region

def execution_time(lst):
    """
    Cálculo del tiempo de ejecución de acuerdo al punto 4 de la prueba, 
    creando la tabla en un dataframe de pandas de acuerdo al punto 5, 
    y mostrando los tiempos (máximo, mínimo, promedio y total) de acuerdo al punto 6.
    Punto 4:
    En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico).
    Punto 5:
    La tabla debe ser creada en un DataFrame con la libreria PANDAS.
    Punto 6:
    Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
    """
    df = pd.DataFrame(lst)
    try:
        total_time, average_time =  df["time"].sum(), df["time"].mean()
        min_time, max_time = df["time"].min(), df["time"].max()
    except KeyError:
        return "error: Dataframe doesn't have the column required"
    return total_time, average_time, min_time, max_time

def countries_json(lst):
    with open('data.json', 'w') as json_file:
        json.dump(lst, json_file)









