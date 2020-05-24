from hashlib import sha1

import json
import pandas as pd 
import requests
import timeit

def obtener_regiones():
    """
    Función para obtener las regiones de la api. 
    Primer punto de la prueba:
    De https://rapidapi.com/apilayernet/api/rest-countries-v1, obtenga todas las regiones existentes.
    """
    regiones = []
    headers = {"x-rapidapi-host": "restcountries-v1.p.rapidapi.com","x-rapidapi-key": "138bf105acmsh9559d0aa02b5a31p15c933jsn73b13c1900e8"}
    res = requests.get('https://restcountries-v1.p.rapidapi.com/all', headers=headers)
    res = res.json()
    for i in res:
        if i['region'] not in regiones and i['region'] is not '':
            regiones.append(i['region'])
        return regiones



def encode_sha1(string, encoding='utf-8'):
    """
    Obteniendo el nombre del idioma en SHA1
    Para el punto tercero
    De https://restcountries.eu/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
    """
    try:
        res = sha1(string.encode(encoding)).hexdigest()
    except AttributeError:
        res = {'error': 'parameter provided is not a string'}
    return res


def obtener_pais_por_region(region):
    """
    Vamos a obtener el primer país que se encuentre en la lista, por cada región. 
    Segundo punto de la prueba:
    De https://restcountries.eu/ Obtenga un pais por region apartir de la region optenida del punto 1.
    """
    tiempo_inicial = timeit.timeit()
    region = region
    res = requests.get(f'https://restcountries.eu/rest/v2/region/{region}')
    res = res.json()
    tiempo_final = timeit.timeit()
    tiempo_total = (tiempo_final - tiempo_inicial)*1000
    pais = {'region': region, 'name': res[0]['name'], 'language': encode_sha1(res[0]['languages'][0]['name']), 'time': tiempo_total}
    return pais

def calculo_tiempo_ejecucion(lst):
    df = pd.DataFrame(lst)
    try:
        tiempo_total, tiempo_promedio =  df["time"].sum(), df["time"].mean()
        tiempo_min, tiempo_max = df["time"].min(), df["time"].max()
    except KeyError:
        return "error: Dataframe doesn't have the column required"
    return tiempo_total, tiempo_promedio, tiempo_min, tiempo_max

def paises_json(lst):
    with open('data.json', 'w') as json_file:
        json.dump(lst, json_file)


