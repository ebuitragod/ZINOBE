from hashlib import sha1

import json
import pandas as pd 
import requests
import timeit

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
                countries_by_region[region] = country
    countries_by_region['time'] = total_time

    return countries_by_region







